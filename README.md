# CS361-Assignment8
CS361: Item Evaluator Microservice for Genshin Impact

HOW TO REQUEST DATA:

1. Include the text file "request.txt" in the same directory as the microservice.
2. Write to "./request.txt" the NUMBER of the artifact. Only input an integer and nothing else. Ensure the .txt file contains nothing but the integer.

Sample call: py sample.py 1

HOW TO RECEIVE DATA:

1. Read from "./request.txt".
2. The microservice will return either crash if the input is not an integer, return an error if the number was not given to any artifact, or return the Roll Distribution for the given artifact.
3. A successfull call will return the evaluation. An unsuccessful one will return an error, and the number of artifacts currently stored in the data.

UML SEQUENCE DIAGRAM:

![image](https://github.com/petpokezorua/CS361-Assignment8/assets/107614682/96ba1f24-2f6c-45ac-8976-9ec0cff772c8)
