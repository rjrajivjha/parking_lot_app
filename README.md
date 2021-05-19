**Parking Lot**

Author : Rajiv Kumar Jha <fork.rajiv@gmail.com> `rjrajivjha`

Problem File : [Link to Problem File](https://docs.google.com/document/d/16WqeWkeRLKCn1JW4hL-4n1Wk-Or_Kt9qUQSC6VawRN0/edit)

What does this app do?
- Create a parking lot
- Park cars to the nearest available slots
- Vacate slots when car leave the parking lot
- Give information related to car, slots and drivers of specific age.
    - return Slot number for Car with given registration number
        `Slot_number_for_car_with_number PB-01-HH-1234`
    - Slot_numbers_for_driver_of_age
        `Slot_numbers_for_driver_of_age PB-01-HH-1234`
    - Vehicle_registration_number_for_driver_of_age
        `Vehicle_registration_number_for_driver_of_age 18`

**Basic Set up**

- Open cloned repository.
  The project is stable over python version >= 3.6.9
- Setup python virtual environment for the project using Pycharm settings (Make sure you create virtual environment 
  outside the project directory to avoid unnecessary errors.)
  ```
  pip3 install virtualenv
  ```
 
  ```
  virtualenv parking_lot
  ```
  
- Activate virtual environment
  ```
  For Ubuntu and Mac: source parking_lot/bin/activate
  ```
  
- Please checkout to master branch before executing following commands.


*How to start the app:*

```
cd parking_lot_app/
git checkout master  #if not already in master.
pip install -r requirements.txt 
cd app/
python -m main 'tests/mocks/input.txt'
```

Sample Input file : tests/mocks/input.txt 

- To test on another file use : 

```
python -m main <absolute_or_relative_path_to_input_file>`
```

*How to run the testcase:*

To run all testcases from project root: `python -m pytest tests/`

To run a single test file :

```
python -m pytest tests/test_file_reader.py
python -m pytest tests/test_runner.py
python -m pytest tests/test_parking_lot.py

```
