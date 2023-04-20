import { Component } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-logs',
  templateUrl: './logs.component.html',
  styleUrls: [ './logs.component.css' ]
})
export class LogsComponent  {
  public Table: User[] = [];
  public Avg: Data[] = [];
  constructor(private http: HttpClient){
    this.http.get('/assets/cvs_test1.csv', {responseType: 'text'})
    .subscribe(
        data => {
            let csvToRowArray = data.split("\n");
            for (let index = 1; index < csvToRowArray.length - 1; index++) {
              let row = csvToRowArray[index].split(",");
              this.Table.push((new User(row[0], row[1], parseFloat(row[2]))));
            }
            console.log(this.Table);
        },
        error => {
            console.log(error);
        }
    );
    this.http.get('/assets/cvs_test1avg.csv', {responseType: 'text'})
    .subscribe(
        data => {
            let csvToRowArray = data.split("\n");
            for (let index = 1; index < csvToRowArray.length - 1; index++) {
              let row = csvToRowArray[index].split(",");
              this.Avg.push((new Data(parseFloat(row[0]), parseFloat(row[1]), parseFloat(row[2]))));
            }
            console.log(this.Avg);
        },
        error => {
            console.log(error);
        }
    );
  }
  

}

export class User{
  date: string;
  time: string;
  voltage: number;

  constructor(date: string, time: string, voltage: number){
    this.date = date;
    this.time = time;
    this.voltage = voltage;
  }
}

export class Data{
    average: number;
    max: number;
    min: number;
  
    constructor(average: number, max: number, min: number){
      this.average = average;
      this.max = max;
      this.min = min;
    }
  }