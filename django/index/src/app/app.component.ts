import { Component } from '@angular/core';
import { ApiService } from './api.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']

})
export class AppComponent {
  usuario = [{title: 'teste'}];
  constructor(private api: ApiService){
    this.getUsuarios();
  }
    getUsuarios =() =>{
      this.api.getAllUsuario(). subscribe(
      data=> {
        this.getUsuarios = data;
      },
      error =>{
        console.log(error)


      }
      )
    }
}
