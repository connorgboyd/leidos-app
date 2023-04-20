import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './home/home.component';
import { GraphsComponent } from './graphs/graphs.component';
import { UsersComponent } from './users/users.component';
import * as CanvasJSAngularChart from '../assets/canvasjs.angular.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'
import { LogsComponent } from './logs/logs.component';
var CanvasJSChart = CanvasJSAngularChart.CanvasJSChart;

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    GraphsComponent,
    UsersComponent,
    CanvasJSChart,
    LogsComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent, LogsComponent]
})
export class AppModule { }
