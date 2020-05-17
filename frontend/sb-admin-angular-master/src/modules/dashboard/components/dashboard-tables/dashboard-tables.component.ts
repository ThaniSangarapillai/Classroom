import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { DashboardService } from '@modules/dashboard/services/dashboard.service';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'sb-dashboard-tables',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: './dashboard-tables.component.html',
    styleUrls: ['dashboard-tables.component.scss'],
})
export class DashboardTablesComponent implements OnInit {
    constructor(private dashboard: DashboardService) {}
    ngOnInit() {
        const table = document.getElementById('dashTable') as HTMLFormElement;
        this.dashboard.hide_tables_store(table);
    }
}
