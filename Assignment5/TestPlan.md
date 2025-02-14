

The test plan for the BMI calculator

Introduction
This test plan describes an approach to testing the BMI Calculator program. The goal is to make sure 
that the program correctly calculates the body mass index based on the data entered by the user and 
classifies it accordingly. The test cases contain both valid and invalid input data to ensure that 
the program handles various scenarios correctly.

Testing Platform
I will use VS Code as the testing platform. VS Code also provides great debugging tools, so if I need 
to debug a specific test, you can use breakpoints and step through the code. 
It allows automated testing, simplifying the verification of functionality and quickly detecting problems.

Test cases

1. Valid Input - Normal Case

Test description: Make sure that the BMI is calculated correctly for acceptable weight and height values.

Initial data: Weight = 150 pounds, height = 5 feet 8 inches

Expected result: Correct BMI value and classification as "Normal weight".


2. Valid Input - Edge Case (Underweight)

Test description: Test the case when the BMI is slightly below normal.

Baseline data: Weight = 100 pounds, height = 5 feet 7 inches

Expected result: BMI should be classified as "Underweight"


3. Invalid Input - Zero Height

Test description: Make sure that the program handles division by zero when the height is 0.

Input data: Weight = 150 lbs, Height = 0 ft 0 inches

Expected result: the program should return a ValueError with a corresponding message.


4. Incorrect Input - Negative weight

Test description: Check how the program handles negative weight values.

Baseline data: Weight = -150 pounds, height = 5 feet 8 inches

Expected result: The program should return an error message or reject the input.


5. Valid Input - High BMI (Obesity)

Test Description: Test a case where BMI is classified as obese.

Baseline data: Weight = 250 pounds, height = 5 feet 4 inches

Expected result: Body mass index should be classified as "Obese"



Execution and reporting

Each test case will be performed using VS Code.

Screenshots of the test runs will be recorded and included in the test plan.

All failed tests will be analyzed and the necessary corrections will be made to the code.
![alt text](<Screenshot 2025-02-14 at 4.15.27 PM.png>)
![alt text](<Screenshot 2025-02-14 at 4.13.28 PM.png>)