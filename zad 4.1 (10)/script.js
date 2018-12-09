//Napisać skrypt, który na aktualnie otwartej stronie internetowej wyszuka wszystkie tabele -->

var table = document.getElementsByTagName("table"); //put all tables from document into variable

//następnie dla każdej tabeli z osobna przejrzy wiersze
// Jeśli w danym (zazwyczaj pierwszym) wierszu znajdują się komórki ​th​​, to ich zawartość (tekst) należy traktować jako etykiety kolumn (​wiersz etykiet)
//Jeśli w wierszu są komórki ​td​​, to ich zawartość traktujemy jako dane (wiersz danych) -->
var tables = [];

for(var i = 0; i<table.length;i++){                             //for every table
    var objectRows = [];                                        //array containing objects that contains rows of the table
    var tr = table[i].getElementsByTagName("tr");               //get all rows from table
    if(tr.length == 0){                                         //if there are no rows in table (== 0) then...
        //console.log("No rows in table");
    }
    else {                                                      //else...
        //console.log("Rows present");
        //console.log(tr.length)
        var labels = null;                                             //variable for latest labels
        for (var j = 0; j<tr.length; j++){                      //for every row in table
            var th = tr[j].getElementsByTagName("th");          //get all <th> tags from row
            var td = tr[j].getElementsByTagName("td");          //get all <td> tags from row
            if (th.length > 0 && td.length == 0 ){              //if there are  only th tags                                 
                labels = th;
                //console.log(labels[1].textContent);
            }
            else if (td.length > 0 && th.length == 0 && labels != null){          //else if there are td tags in table and no th tags
                var data = {};                                  //create object for table's data
                for (var k = 0; k<td.length; k++){              //for every cell in td row
                    if (k < labels.length) var key = labels[k].textContent; //if k is lower than labels collection, assign key name from labels[k]
                    else key = null;                            //else assign key as null
                    var value = td[k].textContent;              //assign value from td[k]
                    //console.log(key + " : " + value);
                    if (key == null || key == "") continue;     //Jeśli etykieta w danej kolumnie jest pusta (złożona wyłącznie z białych znaków), to pomijamy tę kolumnę 
                    else data[key] = value;                          // Z każdego wiersza danych tworzymy obiekt, którego nazwy pól bierzemy z poprzedniego wiersza etykiet -->                                   
                }
                //console.log(" ");
                objectRows.push(data);                              //po czym zachowa ten obiekt w tablicy JS odpowiadającej właśnie przeglądanej tabeli -->
            }
            else continue;                                      //continue if there are no labels and data in table (skip row)
        }
        //#region ORDER NUMBER COLUMN REMOVAL
        var rowsNumber = objectRows.length; //number of rows in array
        for (label in objectRows[0]){       //for every label in table // Tak samo możemy pominąć kolumnę, jeśli zawiera tylko numerację porządkową -->
            for (row in objectRows){        //for every row in table
                if (row == 0) continue;     //if it's first row continue
                else {                      //else...
                    if (isNaN(Number(objectRows[row][label]))==0){ //if value of the current row and label is a number
                        if (row == (rowsNumber - 1) && Number(objectRows[row][label]) - Number(objectRows[row - 1][label]) == 1){ //if it's the last row and (row - (row - 1) = 1) 
                            for (roww in objectRows){                   //for every row in objectRows array
                                //console.log(objectRows[roww].label)
                                delete objectRows[roww][label];         //delete property with "label"
                            }
                            //break;
                        }
                        else if (Number(objectRows[row][label]) - Number(objectRows[row - 1][label]) == 1) continue; //continue if value from current row subtracted by value from previous row == 1
                        else {
                            break;                                                                                   //else break                                                                                  
                        }
                    }
                    else break; //if value of the current row and label isn't a number, break the loop and check next label
                }
            }
        }
        //#endregion 
        if(labels!=null) tables.push(objectRows);               //push array with data objects to array with tables if there are any labels present
    }
}
//tables[numer tabeli][numer wiersza][klucz wiersza(etykieta tabeli)]

//#region TESTY
console.log("=====TESTY=====");

for(i in tables){
    console.log("Tabelka nr " + i );
    for (j in tables[i]){
        for (k in tables [i][j]){
            console.log(k + ": " + tables[i][j][k]); //i - table number, j - row number, k - object key 
        }
    }
}


console.log(tables.length); //== 2 
console.log(tables[0][0]["Nr służbowy"]); //== 9999
console.log(tables[1][0]["Nr służbowy"]); //== undefined
console.log(tables[1][1]["Nr służbowy"]); //== undefined
console.log(tables[1][7]["Nr służbowy"]); //== undefined
for (i in tables[0][0]){
    console.log(i + ": " +  tables[0][0][i]);
}
for (i in tables[1][0]){
    console.log(i + ": " +  tables[1][1][i]);
}
console.log(Object.values(tables[1][7]));

//console.log(tables[0][0]["Nazwisko i imię"]);

//var tds = table[1].getElementsByTagName("td");
//console.log(tds.length);

//#endregion
