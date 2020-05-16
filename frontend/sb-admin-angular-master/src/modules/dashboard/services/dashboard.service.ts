import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable()
export class DashboardService {
    constructor(private http: HttpClient) {}
    posts: any;
    readonly ROOT_URL = 'https://djangobackend-276109.df.r.appspot.com/students/';
    pass = 'X7Mz&&am:&dOhnhk|Oq0$W^MYgkD3V|jgp/17{5=I4QLC:HFpC&P+FgL>Aw-F';
    user = 'TeachingAssistant';


    getDashboard$(): Observable<{}> {
        return of({});
    }
    getPosts() {
        const headerOptions = {
            // headers: new HttpHeaders({
            //     'Content-Type': 'application/json',
            //     'Authorization': 'Basic ' + btoa(this.user + ':' + this.pass),
            // })
        };
        return this.http.post<any>(this.ROOT_URL, {
            discord_name: 'Thani#4847',
            email: 'thanigajan@gmail.com',
        });
    }
}
