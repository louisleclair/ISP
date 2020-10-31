# Homework 2
## Exercise 1: [Attack] cookie Tampering.

[E corp]: https://com402.epfl.ch/hw2/ex1

- Connect to the website [E corp][] and click on the **Hack & Spy** button.
- Open the element inspector and go to the storage category (in Safari), the place where you are going to find the cookies. 
- Find the cookie coming from com402.epfl.ch and copy the Value (The value contains some informations about the session and what you have got from the server after you try to authentificate as **Admin**).
- Use a **base 64 decoder** to decode your value. The result should have the form of (Username, 1602078051, com402, hw1, ex1, user). The first element of the result is the name placed in the Username box during authentification, it must be Username to have a working solution. The second element is the cookie's number session, it is a random number generate for the session. The third, fourth and fifth must remain unchanged and the last one is the level of access you are granted. 
- To break the authentification mechanism, you have to change the authority level granted meaning you have to change **user** by **admin**. The solution has this form: (Username, 1602078051, com402, hw1, ex1, admin) (For clarification the cookie's session number is dependent of your session so it is normal if it is not the same as mine and the parentheses are just here for the presentation).
- Finally you have to encode using a **base 64 encoder** and replace the new value in the value field in the cookies section in the element inspector.
- Now you should be able to access the Hack & Spy and have a Success page.

## Exercise 2: [Defense] HMAC for cookies.

## Exercise 3: [Attack] Client-side password verification.