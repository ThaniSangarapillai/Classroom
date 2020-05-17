import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'sb-dashboard-tables',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: './dashboard-tables.component.html',
    styleUrls: ['dashboard-tables.component.scss'],
})
export class DashboardTablesComponent implements OnInit {
    constructor(private _https: HttpClient) {}
    ngOnInit() {}

    // hide() {
    //     const table = document.getElementById('dashTable') as HTMLFormElement;
    //     table.hidden = true;
    // }
}
