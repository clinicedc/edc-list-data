from __future__ import annotations

from django.apps import AppConfig

from .list_model_maker import ListModelMaker, ListModelMakerError


class LoadListDataError(Exception):
    pass


def load_list_data(
    list_data: dict = None, model_name: str | None = None, apps: AppConfig | None = None
) -> int:
    """Loads data into a list model.

    List models have name, display_name where name
    is the unique field / stored field.

    Format:
        {model_name1: [(name1, display_name),
         (name2, display_name),...],
         model_name2: [(name1, display_name),
         (name2, display_name),...],
        ...}
    """
    if model_name:
        model_names = [model_name]
    else:
        model_names = [k for k in list_data.keys()]
    n = 0
    for model_name in model_names:
        try:
            data = list_data.get(model_name)()
        except TypeError:
            data = list_data.get(model_name)
        try:
            for display_index, row in enumerate(data):
                try:
                    row = row()
                except TypeError:
                    pass
                maker = ListModelMaker(display_index, row, model_name, apps=apps)
                maker.create_or_update()
        except ListModelMakerError as e:
            raise LoadListDataError(f"{e} See {list_data.get(model_name)}.")
        n += 1
    return n
