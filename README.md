# Historic Exchange Rates Microsercive

Edward Leyva <br>
CS361

## Request
In order to request data from my microservice, you need to get an API key. In the place where you need to enter your API_KEY I commented the link where you can get your free one. 
<br> I'll link it here too just in case. https://www.alphavantage.co/support/#api-key <br>

The only place you need to change the code in order to make a request to the API is commented at the bottom. <br> (i.e.. (#Define the currencies you plan to use here) and (#example call to the function))
![image](https://github.com/leyvae/CS-361/assets/83259126/73a18ecd-adfb-4440-a63f-18d4d6cb6e5a)

## Response 
get_historical_data will send a request to the ALPHA VANTAGE services to get the historic exchange rates. You do not have to worry about changing anything other than the places I have detailed above. I highlighted them in purple just for easier viewing.
![image](https://github.com/leyvae/CS-361/assets/83259126/13c4bd42-23fc-419c-bd69-035fb9014df8)

here is an example response shown in the console for viewing the exchange rate between EUR and USD on the date July 25th, 2023
![image](https://github.com/leyvae/CS-361/assets/83259126/4ccda8ff-0c90-4d6a-8d6b-0b63421cedaa)

## UML Sequence for Historic Exchange Rates Microservice
![image](https://github.com/leyvae/CS-361/assets/83259126/5dd5dba5-54cc-45a5-96e2-fed064fae4b1)






