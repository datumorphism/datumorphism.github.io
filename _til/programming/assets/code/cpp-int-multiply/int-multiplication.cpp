#include <iostream>

using namespace std;

int main(int argc, char *argv[]){

   // Check the number of parameters
   if (argc < 1) {
      // Tell the user how to run the program
      std::cerr << "Usage: " << argv[0] << " takes 1 parameter:  the value of int to be multiplied " << std::endl;
      return 1;
   }
   
   int a = stoi(argv[1]);
   long int b = stol(argv[1]);

   cout.precision(10);
   cout << "Multiple itself as int: " << a * a << endl;
   cout << "Multiple itself as long int: " << b * b << endl;



}