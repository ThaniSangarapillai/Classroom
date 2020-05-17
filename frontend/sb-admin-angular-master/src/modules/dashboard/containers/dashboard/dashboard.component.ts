import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { DashboardService } from '@modules/dashboard/services/dashboard.service';

@Component({
    selector: 'sb-dashboard',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: './dashboard.component.html',
    styleUrls: ['dashboard.component.scss'],
})
export class DashboardComponent implements OnInit {
    stuff: any;
    posts: any;
    constructor(private _http: DashboardService) {}
    ngOnInit() {}

    getPosts() {
        this._http.getData().subscribe(data => {
            this.posts = data;
            console.log(data)   
            //return this.stuff;
        });
    }
}
