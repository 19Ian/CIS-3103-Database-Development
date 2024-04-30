import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  PutCommand,
  DynamoDBDocumentClient,
} from "@aws-sdk/lib-dynamodb";

import { v4 as uuidv4 } from 'uuid';

import express from "express" // ALWAYS - npm install express needed

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

async function updateDB(id, first, last, nation, birthdate, foot, height, weight, salary) {
//export const updateDB = async () => {
  console.log("updateDB()");

    const myJSON = [{ ID: "4797", firstName: "Marek"}, 
                    { author: "JFK", role: "President"},
                    { }
                ]
    const theID = uuidv4();

    const putCommand = new PutCommand({
        TableName: "Ian-DB-Project-NoSQL",
        Item: {
            "AthleteID": id,
            FirstName: first,
            LastName: last,
            Nationality: nation,
            BirthDate: birthdate,
            Foot: foot,
            Height: height,
            Weight: weight,
            Salary: salary
        },
      });
      try {
        await docClient.send(putCommand);
        console.log("Item added");
        return theID;
      } catch (err) {
        console.log(err);
        return "Unknown error";
      }
};
// id, first, last, nation, birthdate, foot, height, weight, salary
updateDB("4767", "Marek", "Penksa", "SVK", "1973-08-04", "Either", 181, 68, 0);
updateDB("7302", "Runar", "Normann", "NOR", "1978-03-01", "Left", 182, 75, 0);
updateDB("10764", "Axel", "Wibran", "SWE", "1985-09-09", "Right", 195, 89, 80);
updateDB("103409", "Gary", "Hamilton", "NIR", "1980-10-06", "Right", 176, 77, 2800);
updateDB("103584", "John", "Mousinho", "ENG", "1986-04-30", "Right", 186, 79, 7000);
updateDB("103737", "Adam", "Legzdins", "ENG", "1986-11-23", "Right", 191, 78, 4500);

// const app = express() // ALWAYS

// app.get("/updateDB", function(req, res) {
//   let html = "<h1>Updated DB</h1>"
//   updateDB().then(function(returnVal) {
//     console.log("Returned ID " + returnVal);
//     html += "<p>ID = " + returnVal + "</p>";
//     // send() method returns HTML to the caller / client 
//     res.send(html);
//   });
// });

// app.listen(3000, function() {
//     console.log("Listening on port 3000..."); // RECOMMENDED
//  });