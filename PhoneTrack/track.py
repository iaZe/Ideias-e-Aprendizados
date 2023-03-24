import phonenumbers
from phonenumbers import geocoder, carrier, timezone

mobileNo = input("Digite o número de telefone no formato +5511999999999: ")
mobileNo = phonenumbers.parse(mobileNo)

print(carrier.name_for_number(mobileNo, "pt"))
print(geocoder.description_for_number(mobileNo, "pt"))
print(timezone.time_zones_for_number(mobileNo))
print("Valido: ", phonenumbers.is_valid_number(mobileNo))
print("Possivel: ", phonenumbers.is_possible_number(mobileNo))

