from imageToText import Read, Store_Data

filePath = input("Enter file location: ")
foodInput = input("Enter food name: ")
ingredients = Read(filePath, foodInput)
print(ingredients.ocr())

test = Store_Data(filePath, foodInput)
print(test.dictionary_add())
