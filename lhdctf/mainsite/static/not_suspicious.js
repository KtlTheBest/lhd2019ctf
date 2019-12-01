function compareArrays(a, b){
    if(a.length != b.length) return false;
    for(var i = 0; i < a.length; ++i){
        if(a[i] != b[i]) return false;
    }
    return true;
}

function GetFlag(){
    var guess = window.prompt("Enter the flag:");
    var flag = [153, 10, 148, 12, 136, 60, 173, 61, 181, 35, 178, 42, 248, 77, 211, 90, 196, 104, 244, 121, 239, 96, 235, 57, 130, 18, 136, 4, 149, 30, 204, 123, 241, 124, 247, 37, 151, 29, 129, 22, 148];
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
