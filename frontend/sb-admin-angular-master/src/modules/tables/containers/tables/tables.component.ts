import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
//import { CountryService } from '@modules/tables/services/country.service';

@Component({
    selector: 'sb-tables',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: './tables.component.html',
    styleUrls: ['tables.component.scss'],
})
export class TablesComponent implements OnInit {
    constructor() {}
    ngOnInit() {}
}
