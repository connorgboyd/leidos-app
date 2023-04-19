import { Component } from '@angular/core';
import { UsersService } from '../users.service';
import { User } from '../models/user.model';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent {
  public userInput: User;
  public user: User;

  constructor(private usersService: UsersService) {
    this.userInput = {
      "username": "",
      "password": ""
    };
    this.user = {
      "username": null,
      "password": null
    };
  }
  ngOnInit(): void {
    this.user = {
      "username": null,
      "password": null
    }
  }
 getUser() {
    this.usersService.getUser(this.userInput).subscribe(
      (u) => {
        this.user = u;
        window.alert(this.user);
      }
    );

  }
}



