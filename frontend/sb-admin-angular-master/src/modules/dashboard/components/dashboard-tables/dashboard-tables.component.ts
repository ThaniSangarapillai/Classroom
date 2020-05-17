import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';

@Component({
    selector: 'sb-dashboard-tables',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: './dashboard-tables.component.html',
    styleUrls: ['dashboard-tables.component.scss'],
})
export class DashboardTablesComponent implements OnInit {
    constructor() {}
    ngOnInit() {}

    // hide() {
    //     const table = document.getElementById('dashTable') as HTMLFormElement;
    //     table.hidden = true;
    // }
}
