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
    constructor(private _http: DashboardService) {}
    ngOnInit() {}

    getData() {
        this._http.getPosts().subscribe(data => {
            this.stuff = data;
            return this.stuff;
        });
    }
}
