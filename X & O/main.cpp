#include <iostream>
#include <vector>
#include <string>

// Das Gleiche wie Unten nur in einer Klasse Implementieren ------------------------> Noch Fertigstellen WICHTIG!!!!!!!!!!!!!!!!! <--------------------------------
/*
class X_O{
private:
    std::vector<char> board(9); // Spieboard
    Spieler player[2];
protected:
    bool checkFull(std::vector<char>& board);
public:
    void printBoard();
    void checkWinner();
    void clearBoard(){
        for(unsigned short i{0}; i<board.size(); i++) {
            board[i] = ' '; 
        } 
    }
    void eingabe();
};
*/
void printBoard(std::vector<char>& board){  // Gibt das Spielbrett aus
    //std::cout << "  1   2   3  \n";
    std::cout << "-------------\n";
    std::cout << "| " << board[0] << " | " << board[1] << " | " << board[2] << " |\n";
    std::cout << "-------------\n";
    std::cout << "| " << board[3] << " | " << board[4] << " | " << board[5] << " |\n";
    std::cout << "-------------\n";
    std::cout << "| " << board[6] << " | " << board[7] << " | " << board[8] << " |\n";
    std::cout << "-------------\n";
}
char checkWinner(std::vector<char>& board){ // Ueberpruefen ob es ein Gewinner gibt
    for(unsigned short i{0}; i<9; i += 3){  // Wagrecht
        if(board[i] == board[i+1] && board[i] == board[i+2] && board[i] != ' ') { return board[i]; }
    }
    for(unsigned short i{0}; i<3; i++){     // Senkrecht
        if(board[i] == board[i+3] && board[i] == board[i+6] && board[i] != ' ') { return board[i]; }
    }
    if(board[0] == board[4] && board[0] == board[8] && board[0] != ' ') { return board[0]; }        // Quer
    else if(board[2] == board[4] && board[2] == board[6] && board[2] != ' ') { return board[2]; }
    else { return '#'; }    // Wen kein Gewinner feststeht #=kein Gewinner zurueckgeben
}
bool checkFull(std::vector<char>& board){
    for(unsigned short i{0}; i<board.size(); i++){
        if(board[i] == ' ') { return false; }
    }
    return true;
}
class Spieler{
private:
    char ident;         // 'Identifikationszeichen' (X oder O)
    std::string name;   // Name des Spielers
public:
    char get_ident()const { return ident; }
    std::string get_name()const { return name; }
    void set_ident(char i) { ident = i; }
    void set_name() { std::getline(std::cin, name); }
    unsigned short eingabe(std::vector<char>& board)const {     // Eingabe eingeben + pruefen
        char eing;                                              // Eingabe ist als 'char', da wenn bei int Eingabe man ein char eingibt 'haengt sich das Programm auf
        std::cin >> eing;
        eing--;
        if(board[eing-'0'] != ' ' || (eing-'0') >= board.size()){   // Pruefen ob auf der Stelle am Spielboard nicht schon ein Zeichen ist oder die Eingabe groesser als das Spielfeld ist
            std::cout << "Falsche Eingabe! :(\nVersuchen Sie es bitte noch einmal: ";
            return eingabe(board);                                  // Wen Eingabe falsch ist dann Rekursiv neue Eingabe fordern, bis Sie richtig ist
        }
        return eing-'0';            // Die richtige Eingabe als int zurueckgeben(den charwert 0 davon abziehen) (char)'9'-(char)'0'=(int)9
    }
};
void ausgabeEnde(char winner, Spieler* player){     // Am Ende Mitteilung geben wer gewonnen hat/Ob es Unentschieden ist
    if(winner == player[0].get_ident()){
        std::cout << "Herzlichen Glueckwunsch " << player[0].get_name() << '(' << player[0].get_ident() << ")! Sie haben gewonnen!  :)\n";
    }else if(winner == player[1].get_ident()){
        std::cout << "Herzlichen Glueckwunsch " << player[1].get_name() << '(' << player[1].get_ident() << ")! Sie haben gewonnen!  :)\n";
    }else{
        std::cout << "Unentschieden!\t\t\t:(\n";
    }
}
char Spiel(std::vector<char>& board, Spieler* player){  // Hauptschleife des Spiels
    char winner{'#'};           // Der Gewinner(# bedeutet noch kein Gewinner, X dann fuer den X-Spieler, O fuer den O-Spieler)
    unsigned short turn{0};     // turn=wem sein 'turn' es ist/wer gerade am setzen ist
    printBoard(board);
    while(winner == '#' && !checkFull(board)){      // Abfragen ob schon ein Gewinner feststeht oder ob das Spielfeld voll ist(kein Platz mehr um ein weiteres Zeichen zu setzen)
        std::cout << player[turn].get_name() << '(' << player[turn].get_ident() << ") Eingabe: ";
        board[player[turn].eingabe(board)] = player[turn].get_ident();  // Auf das Feld im Spielfeld, das der Spieler gerade eingegeben hat Sein Zeichen drauf schreiben
        std::cout << "\n\n\n";
        printBoard(board);
        turn = (turn+1) % 2;     // Bestimmt wer gerade an der Reihe ist
        winner = checkWinner(board);    // Ueberpruefen ob es schon einen Gewinner gibt
    }
    return winner;      // Das Spiel ist zu Ende, der Gewinner/Unentschieden steht fest
}
void clearBoard(std::vector<char>& board){          // Das Spielfeld reinigen/nach einem Durchlauf beim 2. Spiel alle Zeichen entfernen
    for(unsigned short i{0}; i<board.size(); i++){
        board[i] = ' ';
    }
}

int main() {
    std::vector<char> board(9); // Spieboard
    Spieler player[2];
    clearBoard(board);
    std::cout << "Name von Spieler1(X): "; player[0].set_name(); player[0].set_ident('X');
    std::cout << "Name von Spieler2(O): "; player[1].set_name(); player[1].set_ident('O');
    while(true){
        char winner = Spiel(board, player); // Hauptspielschleife starten + Gewinner bei Beendigung abspeichern
        ausgabeEnde(winner, player);        // Am Ende die Spieler mitteilen was 
        while(true){
            std::cout << "Noch einmal spielen?[j/n] ";
            char eing; std::cin >> eing;
            if(eing == 'j' || eing == 'J'){ clearBoard(board); break; }
            else if(eing == 'n' || eing == 'N'){ return 0; }
            std::cout << "Falsche Eingabe! :(\n";
        }
    }

    return 0;
}
