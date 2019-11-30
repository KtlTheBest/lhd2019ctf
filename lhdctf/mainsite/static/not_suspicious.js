function compareArrays(a, b){
    if(a.length != b.length) return false;
    for(var i = 0; i < a.length; ++i){
        if(a[i] != b[i]) return false;
    }
    return true;
}

function GetFlag(){
    var guess = window.prompt("Enter the flag:");
    var flag = [180, 37, 181, 61, 171, 58, 162, 112, 197, 91, 210, 76, 224, 124, 241, 103, 232, 99, 177, 10, 154, 0, 140, 29, 150, 68, 243, 121, 244, 127, 173, 31, 149, 9, 158];
    var res = [];
    for(var i = 0; i < flag.length; ++ i){
        var val = 0;
        var userInt = guess.charCodeAt(i);
        if(i == 0) val = userInt ^ 255;
        else {
            val = (255 ^ res[i - 1]) ^ userInt;
        }
        res.push(val);
    }
    if(compareArrays(flag, res)){
        alert("You are correct!!");
    } else {
        alert("Sorry, wrong flag...");
    }
}
