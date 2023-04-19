import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from "@angular/common/http";
import { User } from './models/user.model';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor(private http: HttpClient) { }

  getUser(userInput : User): Observable<User> {
    if(userInput.username == "connor" && userInput.password == "1234"){
      return of(userInput);
    }
    else{
      return of({
        "username": null,
        "password": null
      }); 
    }
    //return this.http.get<SongInfo[]>('https://soundcloud-app-3c43d-default-rtdb.firebaseio.com/song-escuchadasrecientemente.json');

  }
  
 



}
