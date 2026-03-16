def carInfo(car_brand, car_model, **kwargs):
    myCar = {'My_brand': car_brand, 'My_model': car_model,}
    for key, value in kwargs.items():
        myCar[key] = value

    return myCar

myCar = carInfo('Honda', 'Civic', Color='Red', Sport_Package= False)
print(myCar)
