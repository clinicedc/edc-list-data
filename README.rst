|pypi| |travis| |coverage|

edc-list-data
-------------

Populate list data and other static model data on ``Django`` startup.

To install add ``edc_list_data.apps.AppConfig`` to your `INSTALLED_APPS`, then create a ``list_data.py`` in the root of your app.

Most commonly used to populate M2M data known here as ``list_data``. M2M field models should use the ``ListModelMixin``.

For example:

.. code-block:: python

	class Antibiotic(ListModelMixin, BaseUuidModel):

	    class Meta(ListModelMixin.Meta):
	        pass


An example ``list_data.py``:


.. code-block:: python
	
	from edc_constants.constants import OTHER
	from edc_list_data import PreloadData

	list_data = {
	    'my_lists_app.antibiotic': [
	        ('flucloxacillin', 'Flucloxacillin'),
	        ('gentamicin', 'Gentamicin'),
	        ('ceftriaxone', 'Ceftriaxone'),
	        ('amoxicillin_ampicillin', 'Amoxicillin/Ampicillin'),
	        ('doxycycline', 'Doxycycline'),
	        ('erythromycin', 'Erythromycin'),
	        ('ciprofloxacin', 'Ciprofloxacin'),
	        (OTHER, 'Other, specify')
	    ],
	}

	preload_data = PreloadData(list_data=list_data)


``PreloadData`` will persist the list data in model ``Antibiotic`` and maintain the order in which the list items are declared.

See also call to ``site_list_data.autodiscover`` called in ``edc_list_data.apps.AppConfig``.



.. |pypi| image:: https://img.shields.io/pypi/v/edc-list-data.svg
    :target: https://pypi.python.org/pypi/edc-list-data
    
.. |travis| image:: https://travis-ci.org/clinicedc/edc-list-data.svg?branch=develop
    :target: https://travis-ci.org/clinicedc/edc-list-data
    
.. |coverage| image:: https://coveralls.io/repos/github/clinicedc/edc-list-data/badge.svg?branch=develop
    :target: https://coveralls.io/github/clinicedc/edc-list-data?branch=develop
