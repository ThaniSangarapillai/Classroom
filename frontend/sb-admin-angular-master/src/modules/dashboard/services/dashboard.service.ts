import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Country } from '@modules/tables/models/tables.model';
import { Observable, of } from 'rxjs';

@Injectable()
export class DashboardService {
    constructor(private http: HttpClient) {}
    posts!: Observable<Country[]>;
    readonly ROOT_URL = 'http://127.0.0.1:8000/students/';
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
        this.posts = this.http.post<Country[]>(this.ROOT_URL, {
            discord_name: 'Thani#4847',
            email: 'thanigajan@gmail.com',
        });
        return this.posts;
    }
}
