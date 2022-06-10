hexMap = new Map([[0, "0"], [1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "a"], [11, "b"], [12, "c"], [13, "d"], [14, "e"], [15, "f"]])

function decBin(n) {
    let s=""

    if(n === 0) {
        return 0
    }
    else {
        while(n != 0) {
            if (n%2 === 0) {
                s = "0" + s
                n = n/2
            }
            else {
                s = "1" + s
                n = (n-1)/2
            }
        }
        return s
    }

}

function binDec(n) {
    let longueur = n.length
    let result = 0
    for(let i = 0 ; i < longueur; i++) {
        result = result + parseInt(n.charAt(i)) * 2 ** (longueur - (i + 1))
    }
    return result
}

function decHex(n) {
    let result =""
    while(n != 0) {
        reste = n%16
        result = hexMap.get(reste) + result
        n = Math.floor(n/16)
    }
    return result
}

function hexDec(n) {
    result = parseInt(n, 16)
    return result
}

function conversionDec() {
    n = document.getElementById("decField").value // récupère la valeur du champ décimal et le stocke dans n
    document.getElementById("hexField").value = decHex(n) // Convertit le nombre n en hexadécimal et change la valeur du champ Hexédacimal
    document.getElementById("binField").value = decBin(n) // Convertit le nombre n en binaire et change la valeur du champ Binaire
}

function conversionBin() {
    n = document.getElementById("binField").value // récupère la valeur du champ Binaire et le dtocke dans n
    document.getElementById("decField").value = binDec(n) // Convertit le nombre n en Décimal et change la valeur du champ Décimal
    document.getElementById("hexField").value = decHex(binDec(n)) // Convertit le nombre n en Décimal, puis en hexadécimal et change la valeur du champ Hexédacimal
}

function conversionHex() {
    n = document.getElementById("hexField").value // récupère la valeur du champ hexadécimal et le stocke dans n
    document.getElementById("decField").value = hexDec(n) // Convertit le nombre n en Décimal et change la valeur du champ Décimal
    document.getElementById("binField").value = decBin(hexDec(n))// Convertit le nombre n en décimal, puis en binaire et change la valeur du champ Binaire
}