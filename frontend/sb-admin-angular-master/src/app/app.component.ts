import { Component } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ChildActivationEnd, Router } from '@angular/router';
import { filter } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss'],
})
export class AppComponent {
    title = 'sb-admin-angular';
    posts: any;
    readonly ROOT_URL = 'https://jsonplaceholder.typicode.com/todos/1';

    constructor(public router: Router, private titleService: Title, private http: HttpClient) {
        this.router.events
            .pipe(filter(event => event instanceof ChildActivationEnd))
            .subscribe(event => {
                let snapshot = (event as ChildActivationEnd).snapshot;
                while (snapshot.firstChild !== null) {
                    snapshot = snapshot.firstChild;
                }
                this.titleService.setTitle(snapshot.data.title || 'SB Admin Angular');
            });
    }

    getPosts() {
        this.posts = this.http.get(this.ROOT_URL + '/posts');
    }

    
}
