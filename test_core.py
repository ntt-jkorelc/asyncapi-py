from asyncapi.core import (
    Contact,
    Correlation,
    License,
)

contact = Contact.from_json("tests/data/contact.json")
print(contact.model_dump())

contact = Contact.from_yaml("tests/data/contact.yaml")
print(contact.model_dump())


correlate = Correlation.from_json("tests/data/correlation.json")
correlate = Correlation.from_yaml("tests/data/correlation.yaml")


license = License.from_json("tests/data/license.json")
print(license)

license = License.from_yaml("tests/data/license.yaml")
print(license)
