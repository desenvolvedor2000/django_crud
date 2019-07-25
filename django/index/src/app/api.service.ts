import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl="http://127.0.0.1:8000";
  httpHeaders = ({'Content-type': 'application/json'});

  constructor(private http: HttpClient) { }
 
  getAllUsuario():Observable<any>{
    return this.http.get(this.baseurl+'/usuarios/', {headers:this.httpHeaders});
  }
  
}
