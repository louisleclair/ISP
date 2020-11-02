if (username.length > 100) {
    alert("There's a difference between knowing the path and walking the path.");
        return;
    } 
else if (password.length > 100) {
    alert("The best answer to anger is silence.");
        return;
}
if (password != hash(username,mySecureOneTimePad)) {
    alert("I didn't say it would be easy, Neo. I just said it would be the truth.");
        return;
}