#include <iostream>
#include <fstream>
#include <string>
#include <openssl/crypto.h>

using namespace std;

int main(int argc, char* argv[]){

    // Check if the filename is provided as a command-line argument
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <filename>" << endl;
        return 1;
    }

    // Declare known plain and cipher text
    string plaintext = "This is a top secret.";
    string knownCipher = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9";

    // Create fstream object and open file
    ifstream file(argv[1]);

    if (!file.is_open()){
        cerr << "Error opening file " << argv[1] << endl;
        return 1; 
    }

    string line;
    while (getline(file, line)){
        
        // Encrypt plaintext with line from dictionary

    }

    /*For every word in the dictionary file, we need to see if that word is the 
    proper key. We can call openssl aes-cbc to see if the ciphertext matches with the given key
    */



    // Return value from main
    return 0;
}