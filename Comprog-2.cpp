#include <iostream>
#include <string>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <fstream>
using namespace std;



struct Information {
    string Fname, Lname, Mname, address;
    char gender, NOname;
    string PIN;
    int month,day,year;
    float iniDeposit;
    float Current;
    char TypeAcc;
    int accNum;
    bool accCreated;
};

struct Node {
    Information info;
    Node* next;
};

Node* head = nullptr;

void addRecord(const Information& info) {
    Node* newNode = new Node;
    newNode->info = info;
    newNode->next = head;
    head = newNode;
}

void PINcheck(Information& info);
void account(Information& info);
void ViewAcc (Information& info);
void openFile(Information& info);
void CloseAcc(Information& info);
void Deposit(Information &info);
void Withdraw(Information &info);
void Balance(Information &info);
void Menu(Information& info);
bool ValidName (const string& name);

int main() {
	Information info;
    Menu(info);
    return 0;
}

void Menu(Information& info) {
	string choice;
	char choice1;
    string menu[7] = {"Open Account","View Account Information", "Deposit", "Withdraw", "Check Balance", "Close Account", "Exit Program"};
    cout << "=== Banking System Menu ===" << endl;
    for (int i = 0; i < 7; i++) {
        cout << "[" << i + 1 << "] " << menu[i] << endl;
    }
    cout << "==========================" << endl;
    cout << "Enter your choice (1-7): ";
    do {
        cin >> choice;
        if (choice.length() != 1) {
        	cout << "Invalid Choice" << endl;
        	cin.clear();
        	cin.ignore();
		}else{
			choice1 = choice[0];
        switch (choice1) {
        	case '1':
                account(info);
                break;
            case '2':
                ViewAcc(info);
                break;
            case '3':
                Deposit(info);
                break;
            case '4':
                Withdraw(info);
                break;
            case '5':
                Balance(info);
                break;
            case '6':
                CloseAcc(info);
                break;
            case '7':
                cout << "Exiting the program" << endl;
                exit(EXIT_SUCCESS);
                break;
            default:
                cout << "Invalid choice" << endl;
                break;
        }
    }
    } while (true);
    
}
    

void account(Information& info) {
    string pin, monthInput, dayInput, yearInput, fnamein, lnamein, mnamein;
    int age;
    cout << "Birthdate (0/00/0000)" << endl;
    do {
        cout << "Month: ";
        cin >> monthInput;
        cin.ignore();
        bool validmonth = true;

        for (char c : monthInput) {
            if (!isdigit(c)) {
                validmonth = false;
                cout << "Please enter a valid month (01 - 12)." << endl;
                break;
            }
        }

        if (validmonth) {
            int month = stoi(monthInput);
            if (month >= 1 && month <= 12) {
                info.month = month;
                break;
            } else {
                cout << "Invalid month. Please enter a number between 1 and 12." << endl;
            }
        }
    } while (true);
    
    do {
        cout << "Day: ";
        cin >> dayInput;
        cin.ignore();
        bool validday = true;

        for (char b : dayInput) {
            if (!isdigit(b)) {
                validday = false;
                cout << "Please enter a valid day (01 - 31)." << endl;
                break;
            }
        }

        if (validday) {
            int day = stoi(dayInput);
            if (day >= 1 && day <= 31) {
                info.day = day;
                break;
            } else {
                cout << "Invalid day. Please enter a number between 1 and 31." << endl;
            }
        }
    } while (true);

    do {
        cout << "Year: ";
        cin >> yearInput;
        cin.ignore();
        bool validyear = true;

        for (char a : yearInput) {
            if (!isdigit(a)) {
                validyear = false;
                cout << "Please enter a valid year" << endl;
                break;
            }
        }

        if (validyear) {
            int year = stoi(yearInput);
            if (year >= 1920 && year <= 2024) {
                info.year = year;
                break;
            } else {
                cout << "Invalid year." << endl;
            }
        }
    } while (true);
    age = 2024 - info.year;

    if (info.month < 4 || (info.month == 4 && info.day > 2)) {
        age--;
    }

    if (age >= 18) {
        cout << "You may continue " << endl << endl;
    } else {
        cout << "You are under 18, access denied";
        exit(EXIT_SUCCESS);
    }

    do {
        cout << "Enter your 6-digit PIN number: ";
        cin >> pin;
        cin.ignore();
        system("cls");

        if (pin.length() != 6) {
            cout << "PIN length must be 6 digits" << endl;
        } else {
            bool valid = true;
            for (char d : pin) {
                if (!isdigit(d)) {
                    valid = false;
                    cout << "PIN should only include numbers" << endl;
                    break;
                }
            }
            if (valid) {
            	info.PIN = pin;
                cout << "PIN successfully set: " << info.PIN << endl << endl;
                break;
            }
        }
    } while (true);

    do {
        cout << "First name: ";
        getline(cin, info.Fname);
        if (!ValidName(info.Fname)) {
            cout << "Please enter a valid name." << endl;
        }
    } while (!ValidName(info.Fname));

    do {
    	cout << "Do you have a middle name [Y/N]: ";
    	cin >> info.NOname;
    	cin.ignore();
		if (info.NOname == 'N' || info.NOname == 'n') {
    		break;
			}
		if (info.NOname == 'Y' || info.NOname == 'y') {
    		cout << "Middle name: ";
    		cin >> info.Mname;
    		cin.ignore();
			break;
			}
        if (!ValidName(info.Mname)) {
            cout << "Please enter a valid name." << endl;
        }
    } while (!ValidName(info.Mname));

    do {
        cout << "Last name: ";
        getline(cin, info.Lname);
        if (!ValidName(info.Lname)) {
            cout << "Please enter a valid last name." << endl;
        }
    } while (!ValidName(info.Lname));

	cout << "Full Address: ";
    getline(cin, info.address);
    system("cls");

    do {
        cout << "Gender (m/f): ";
        cin >> info.gender;
        cin.ignore();
        system("cls");
        if (info.gender != 'm' && info.gender != 'M' && info.gender != 'F' && info.gender != 'f') {
            cout << "Input is not included in the options" << endl;
        }
    } while (info.gender != 'm' && info.gender != 'M' && info.gender != 'F' && info.gender != 'f');

    do {
        cout << "Account Type (Savings[S]/Current[C]): ";
        cin >> info.TypeAcc;
        cin.ignore();
        system("cls");
    } while (info.TypeAcc != 'S' && info.TypeAcc != 'C' && info.TypeAcc != 's' && info.TypeAcc != 'c');

    if (info.TypeAcc == 'S' || info.TypeAcc == 's') {
        do {
            cout << "Enter initial deposit (Min. PHP 5,000): ";
            cin >> info.iniDeposit;
            info.Current = info.iniDeposit;
            cin.ignore();
            if (info.iniDeposit < 5000) {
                cout << "Initial deposit is below the minimum amount" << endl;
            }
            system("cls");
        } while (info.iniDeposit < 5000);
    } else if (info.TypeAcc == 'C' || info.TypeAcc == 'c') {
        do {
            cout << "Enter initial deposit (Min. PHP 10,000): ";
            cin >> info.iniDeposit;
            info.Current = info.iniDeposit;
            cin.ignore();
            system("cls");
            if (info.iniDeposit < 10000) {
                cout << "Initial deposit is below the minimum amount" << endl;
            }
        } while (info.iniDeposit < 10000);
    }
    info.accCreated = true;
    srand(time(0));
    int random;
    random = 100000000 + rand() % 899999990;
    info.accNum = random;
    addRecord(info);
    openFile(info);
    Menu(info);
}

void openFile(Information& info) {
    string filename = to_string(info.accNum) + ".txt";
    ofstream bank(filename);
    if (!bank.is_open()) {
        cerr << "Error opening file " << filename << " for writing!" << endl;
        return;
    }
    bank << "Account information:" << endl;
    	if (info.NOname == 'n' || info.NOname == 'N'){
    		bank << "Full Name: " << info.Fname << " " << info.Lname << endl;
		}
		else{
			bank << "Full Name: " << info.Fname << " " << info.Mname << " " << info.Lname << endl;
		}
    bank << "Address: " << info.address << endl;
    bank << "Birthdate: " << info.month << "/" << info.day << "/" << info.year << endl;
    bank << "Gender: " << info.gender << endl;
    bank << "Account type: " << (info.TypeAcc == 'S' || info.TypeAcc == 's' ? "Savings" : "Current") << endl;
    bank << "Initial deposit: " << info.iniDeposit << endl;
    bank << "Current Balance: " << info.Current << endl;
    bank.close();
    Menu(info);
}

void PINcheck(Information& info){
	string PIN;
	int counter = 0;
	char option;
	do{
		cout << "Enter PIN: ";
		cin >> PIN[0] >> PIN[1] >> PIN[2] >> PIN[3] >> PIN[4] >> PIN[5];
		
		if (info.accCreated == false){	
		cout << "Create an account first" << endl;
		cout << "-----------------------" << endl << endl;
		Menu(info);
	    }
        if (PIN[0] != info.PIN[0] || PIN[1] != info.PIN[1] || PIN[2] != info.PIN[2] || PIN[3] != info.PIN[3] || PIN[4] != info.PIN[4] || PIN[5] != info.PIN[5] ) {
            counter++;
            if (counter == 3) {
                cout << "Your account is now blocked";
                exit(EXIT_SUCCESS);
            } else {
                cout << "Incorrect PIN. You have " << abs(3 - counter) << " more tries." << endl;
                cout << info.PIN << " " << PIN << endl;
            }
        } else if (PIN[0] == info.PIN[0] && PIN[1] == info.PIN[1] && PIN[2] == info.PIN[2] && PIN[3] == info.PIN[3] && PIN[4] == info.PIN[4] && PIN[5] == info.PIN[5] && PIN[6] == info.PIN[6]){
            cout << "Correct PIN entered. Access granted." << endl << endl;
            break;
        }
	}while(counter < 3);
}

void CloseAcc(Information& info){
    string filename = to_string(info.accNum) + ".txt";
    
    if (remove(filename.c_str()) != 0) {
        cout << "Error: Cannot close account. File '" << filename << "' could not be removed." << endl;
    } else {
        cout << "Account successfully closed. File '" << filename << "' deleted." << endl;
    }
    Menu(info);
}

void ViewAcc(Information& info) {
	PINcheck(info);
    char option2;

    if (info.accCreated){
        cout << "Account information" << endl;
        if (info.NOname == 'n' || info.NOname == 'N'){
    		cout << "Full Name: " << info.Fname << " " << info.Lname << endl;
		}
		else{
			cout << "Full Name: " << info.Fname << " " << info.Mname << " " << info.Lname << endl;
		}
        cout << "Address: " << info.address << endl;
        cout << "Birthday: " << info.month << "/" << info.day << "/" << info.year << endl;
        cout << "Gender: " << info.gender << endl;
        cout << "Account type: ";
        if (info.TypeAcc == 's' || info.TypeAcc == 'S') {
            cout << "Savings" << endl;
        } else if (info.TypeAcc == 'C' || info.TypeAcc == 'c') {
            cout << "Current" << endl;
        }
        cout << "Initial deposit: " << info.iniDeposit << endl;
        cout << "Current Balance: " << info.Current << endl;
        cout << "----------------------------------------------------------------------" << endl << endl;

    }else{
    	cout << "\nCreate an account first" << endl;
    	cout << "---------------------------" << endl << endl;
    	Menu(info);
	}

    do {
        cout << "Returning to the Menu [Y]: ";
        cin >> option2;
        if (option2 == 'y' || option2 == 'Y') {
            Menu(info);
        }
    } while (option2 != 'Y' && option2 != 'y');
}

void Deposit(Information &info){
    PINcheck (info);
    int depo;
    char confirm;
    char option;
    char option2;
    switch (info.TypeAcc){
        case 's':
        case 'S': {
            do {
                cout << "How much would you like to Deposit?(Minimum of 300)\n: ";
                cin >> depo;
                cout << "[Y] Continue"<<endl;
				cout << "[N] Go Back to Menu"<<endl;
                cout << ":";
                cin >> confirm;
                if (confirm == 'Y' || confirm == 'y'){
                    if (depo < 300){
                        cout << "Entered amount is not valid";
                		cout << "[Y] Continue"<<endl;
						cout << "[N] Go Back to Menu"<<endl;
                        cin >> option;
                        if (option == 'n' || option == 'N'){
                            Menu(info);
                        }
                    } else {
                        info.Current = info.Current + depo;
                        cout << "Transaction is successful. \nRemaining balance:" << info.Current;
                        cout << "\n---------------------------------------------------" << endl << endl;
                        openFile(info);
                        do {                     
                            cout << "Returning to the Menu [Y]: ";
                            cin >> option2;
                            if (option2 == 'y' || option2 == 'Y'){
                                Menu(info);
                            }	
                        } while (option2 != 'Y' && option2 != 'y');
                    }
                } else {
                    Menu(info);
                }
            } while (option == 'y' || option == 'Y');
            break;
        }
        case 'C':
        case 'c': {
            do {
                cout << "How much would you like to Deposit?(Minimum of 500)\n: ";
                cin >> depo;
                cout << "[Y] Confirm"<<endl;
				cout << "[N] Go Back to Menu"<<endl;
                cout << ":";
                cin >> confirm;
                if (confirm == 'Y' || confirm == 'y'){
                    if (depo < 500){
                        cout << "Entered amount is not valid";
                        cout << "[Y] continue or [N] Go back to Menu: ";
                        cin >> option;
                        if (option == 'n' || option == 'N'){
                            Menu(info);
                        }
                    } else {
                        info.Current = info.Current + depo;
                        cout << "Transaction is successful. \n Remaining balance: " << info.Current;
                        cout << "---------------------------------------------------" << endl << endl;
                        openFile(info);
                        do {                     
                            cout << "Returning to the Menu [Y]: ";
                            cin >> option2;
                            if (option2 == 'y' || option2 == 'Y'){
                                Menu(info);
                            }	
                        } while (option2 != 'Y' && option2 != 'y');
                    }
                } else {
                    Menu(info);
                }
            } while (option == 'y' || option == 'Y');
            break;
        }
    }
}

void Withdraw(Information &info){
    PINcheck (info);
    int withdraw;
    char confirm;
    char option;
    char option2;
    switch (info.TypeAcc){
        case 's':
        case 'S': {
            do {
                cout << "How much would you like to Withdraw?(Minimum of 300)\n: ";
                cin >> withdraw;
                cout << "[Y] Continue [N] Go Back to Menu"<<endl;
                cout << ":";
                cin >> confirm;
                if (confirm == 'Y' || confirm == 'y'){
                    if (withdraw < 300){
                        cout << "Entered amount is not valid";
                        cout << "[Y] continue or [N] Go back to Menu: ";
                        cin >> option;
                        if (option == 'n' || option == 'N'){
                            Menu(info);
                        }
                    } else {
                        info.Current = info.Current - withdraw;
                        cout << "Transaction is successful. \nRemaining balance:" << info.Current;
                        cout << "\n---------------------------------------------------" << endl << endl;
                        openFile(info);
                        do {                     
                            cout << "Returning to the Menu [Y]: ";
                            cin >> option2;
                            if (option2 == 'y' || option2 == 'Y'){
                                Menu(info);
                            }	
                        } while (option2 != 'Y' && option2 != 'y');
                    }
                } else {
                    Menu(info); 
                }
            } while (option == 'y' || option == 'Y');
            break;
        }
        case 'C':
        case 'c': {
            do {
                cout << "How much would you like to Withdraw?(Minimum of 500)\n: ";
                cin >> withdraw;
                cout << "[Y] Continue [N] Go Back to Menu"<<endl;
                cout << ":";
                cin >> confirm;
                if (confirm == 'Y' || confirm == 'y'){
                    if (withdraw < 500){
                        cout << "Entered amount is not valid";
                        cout << "[Y] continue or [N] Go back to Menu: ";
                        cin >> option;
                        if (option == 'n' || option == 'N'){
                            Menu(info);
                        }
                    } else {
                       info.Current = info.Current - withdraw;
                        cout << "Transaction is successful. \n Remaining balance: " << info.Current;
                        cout << "\n---------------------------------------------------" << endl << endl;
                        openFile(info);
                        do {                     
                            cout << "Returning to the Menu [Y]: ";
                            cin >> option2;
                            if (option2 == 'y' || option2 == 'Y'){
                                Menu(info);
                            }	
                        } while (option2 != 'Y' && option2 != 'y');
                    }
                } else {
                    Menu(info);
                }
            } while (option == 'y' || option == 'Y');
            break;
        }
    }
}

void Balance(Information &info){
	PINcheck (info);
	char option;
	cout << "Remaining Balance: " << info.Current << endl;
	cout << "--------------------------------" << endl << endl;
	do{
	cout << "Returning to the Menu [Y]: ";
	cin >> option;
	 if (option == 'y' || option == 'Y'){
		Menu(info);
	 }		
	} while (option != 'Y' && option != 'y');

	Menu(info);
}

bool ValidName (const string& name){
	for (char c: name) {
		if (!isalpha(c) && c!= ' '){
			return false;
		}
	}
	return true;
}