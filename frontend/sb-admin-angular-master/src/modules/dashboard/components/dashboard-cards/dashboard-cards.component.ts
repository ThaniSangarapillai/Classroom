import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
//import { DashboardService } from '@modules/dashboard/services/dashboard.service';

@Component({
    selector: 'sb-dashboard-cards',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: './dashboard-cards.component.html',
    styleUrls: ['dashboard-cards.component.scss'],
})
export class DashboardCardsComponent implements OnInit {
    constructor(
        // private _http: DashboardService
        ) {}
    ngOnInit() {
        //this._http.hide_tables();
    }
}
