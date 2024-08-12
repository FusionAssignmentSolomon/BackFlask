Backend, to run it just start the main. (I used python12 but python 3.9 will for)

Tried to make the best design but I screwed because I understood later that I need to use also websockets. 
First I made a RestfulAPI project that would work on HTTP request and only after relized it was partliy wrong.
As I wrote in the FE repo readmy, some of the logic should use HTTP and other (The game itself) websockets.


* Because I was short on time I didn't implement the Postman side. If I had more time I would create a right DTO for each request so in the response it will be a nice JSON that represents the board, who turn it is and if there is a Winner or draw.
