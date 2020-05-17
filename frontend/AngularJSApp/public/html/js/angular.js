// import { link } from "fs";
// import { homedir } from "os";

// angular.module('ngMaterial', ["ng","ngAnimate","ngAria"]);

var app = angular.module('app', ['ngRoute']);

app.config(function ($routeProvider) {
    $routeProvider
        // the routing between different pages
        .when("/home", {
            templateUrl: "/html/profile.html",
            controller: "homeController",
        })
        .when("/dashboard", {
            templateUrl: "/html/dashboard.html",
            controller: "dashController",
        })

        .when("/students", {
            templateUrl: "/html/basic-table.html",
            controller: "studentController",
        })
        .when("/word", {
            templateUrl: "/html/word-table.html",
            controller: "wordController",
        })

        .when("/reminders", {
            templateUrl: "/html/reminders-table.html",
            controller: "remindersController",
        })

        .otherwise({
            redirectTo: '/home'
        });



});

app.controller('studentController', ['$scope', '$http', '$location', function ($scope, $http, $location) {
    $scope.students = []
    $scope.student = {'name':'', 'discord_name':''}

    $scope.update = function () {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/students/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com" },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.students = response.data
                    console.log(response.data)
                } else {

                    console.log("ohno!")
                }
            });
    };

    $scope.delete = function (name, discord) {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/remove/student/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com", "student": { "name": name, "discord_name": discord } },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    console.log("woo!")
                } else {

                    console.log("ohno!")
                }
            })
    }

    $scope.add = function (name, discord_name) {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/add/student/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com", "student": { "name": name, "discord_name": discord_name } },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.update()
                } else {

                    console.log("ohno!")
                }
            })
    }

    $scope.update();
}]);

app.controller('wordController', ['$scope', '$http', '$location', function ($scope, $http, $location) {
    $scope.words = []
    $scope.word = {}

    $scope.update = function () {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/filterwords/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com" },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.words = response.data
                    console.log(response.data)
                } else {

                    console.log("ohno!")
                }
            });
    };

    $scope.delete = function (word) {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/remove/word/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com", "word": {"word": word}},
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.update();
                }
            })
    }

    $scope.add = function (word) {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/add/word/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com", "word": {"word": word}},
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.update();
                    word = '';
                }
            })
    }

    $scope.update();
}]);

app.controller('profileController', ['$scope', '$http', '$location', function ($scope, $http, $location) {
    $scope.update = function () {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/filterwords/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com" },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.words = response.data
                    console.log(response.data)
                }
            });
    };

    $scope.update();
}]);
``

app.controller('remindersController', ['$scope', '$http', '$location', function ($scope, $http, $location) {
    console.log("hi");

    $scope.reminders = []
    $scope.student = {'name':'', 'discord_name':''}

    $scope.update = function () {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/reminders/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com" },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    reminders = response.data
                    $scope.reminders = []
                    for (let x in reminders) {
                        console.log(x)
                        $scope.reminders.push({"text":reminders[x].text, "date_time": reminders[x].date_time.replace("T", " ").replace("Z","")})
                    }
                } else {

                    console.log("ohno!")
                }
            })
            .then(function () {
                
            });
    };

    $scope.delete = function (indice) {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/remove/reminder/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com", "pk": indice },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.update();
                } else {

                    console.log("ohno!")
                }
            })
    }

    $scope.modify = function (text, date_time, indice) {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/modify/reminder/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com", "reminder":{"pk": indice, "text":text, "date_time":date_time }},
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.buttonHide = false
                    $scope.update();
                } else {

                    console.log("ohno!")
                }
            })
    }

    $scope.add = function (text, date_time) {
        $http({
            method: 'POST',
            url: "http://34.125.57.52/add/reminder/",
            data: { 'discord_name': "Thani#4847", "email": "thanigajan@gmail.com", "reminder":{"text":text, "date_time":date_time } },
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    $scope.update()
                } else {

                    console.log("ohno!")
                }
            })
    }

    $scope.update();
}]);
// var checkRouting = function ($q, $window, $location, $http) {
//     console.log("HEYO");
//     var deferred = $q.defer();
//     console.log("heyo2");
//     $http.post("http://127.0.0.1:8080/user_api/logged", { checkLogged: "true" })
//         .then(function (response) {
//             console.log(response);
//             if (response.status == 200) {
//                 deferred.resolve(true);
//             } else {
//                 deferred.reject();
//                 $location.path("/login");
//             }
//         },
//             function (response) {
//                 deferred.reject();
//                 $location.path("/login");
//             }
//         );
//     console.log("heyo3");
//     return deferred.promise;

// };


// var checkRoutingAdmin = function ($q, $window, $location, $http) {
//     console.log("HEYO");
//     var deferred = $q.defer();
//     console.log("heyo2");
//     $http.post("http://127.0.0.1:8080/user_api/loggedAdmin", { checkLogged: "true" })
//         .then(function (response) {
//             console.log(response);
//             if (response.status == 200) {
//                 deferred.resolve(true);
//             } else {
//                 deferred.reject();
//                 $location.path("/login");
//             }
//         },
//             function (response) {
//                 deferred.reject();
//                 $location.path("/login");
//             }
//         );
//     console.log("heyo3");
//     return deferred.promise;

// };

// app.controller('registerController', ['$scope', '$http', '$location', function ($scope, $http, $location) {
//     console.log("hi");

//     $scope.hello = function () {
//         console.log($scope.form.user);
//         $http({
//             method: 'POST',
//             url: "http://127.0.0.1:8080/user_api/check",
//             data: { 'user': $scope.form.user }
//         })
//             .then(function (response) {
//                 console.log(response);
//                 if (response.data.results.status === "true") {
//                     $scope.usertaken = true;
//                 } else if (response.data.results.status === 'false') {
//                     $scope.usertaken = false;
//                     $http({
//                         method: 'POST',
//                         url: "http://127.0.0.1:8080/user_api/register",
//                         data: $scope.form
//                     })

//                         .then(function (response) {
//                             console.log(response);
//                             $location.path('/login');
//                         });
//                 } else {

//                 }
//             });
//     };
// }]);

// app.controller("signinController", ['$scope', '$rootScope', '$http', '$location', '$localStorage', '$window', '$routeParams', function ($scope, $rootScope, $http, $location, $localStorage, $window, $routeParams) {

//     console.log($location.search());
//     var query = $location.search();

//     if (query && query.redirectFrom) {
//         $rootScope.showerror = true;
//     } else {
//         $rootScope.showerror = false;
//     }

//     $scope.login = function () {
//         $http(
//             {
//                 method: 'POST',
//                 url: 'http://127.0.0.1:8080/user_api/signin',
//                 data: { username: $scope.form.username, password: $scope.form.password }
//             })
//             .then(function (response) {
//                 console.log(response.data.results);
//                 if (response.data.results.status) {
//                     $window.localStorage.setItem("user", JSON.stringify({ "username": response.data.username, "token": response.data.token, "firstname": response.data.firstname, "lastname": response.data.lastname, "email": response.data.email, permissions: response.data.permissions }));
//                     $http.defaults.headers.common.authorization = response.data.token;
//                     $rootScope.loginhide = true;
//                     console.log($rootScope.loginhide);

//                     {
//                         if (query && query.redirectFrom) {
//                             $location.path(query.redirectFrom);
//                         } else {
//                             $location.path('/home');
//                         }
//                     }
//                 } else {
//                     console.log("Incorrect");
//                     $scope.form.reset();
//                 }
//                 console.log($window.localStorage.getItem("user"));

//             });
//     };

// }]);

// ////////////////////////Home////////////////////////
// app.controller('homeController', function ($scope, $http) {
//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/home").then(function (response) {
//             console.log(response);
//             $scope.home = response.data;
//         });
//     }

//     $scope.update();
// });
// ///////////////////////////////////////////////////////

// ////////////////////////Home-Admin////////////////////////
// app.controller('homeAdminController', function ($scope, $http, factory) {
//     $scope.home = {};
//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/home").then(function (response) {
//             console.log(response);
//             $scope.home = response.data;
//         });
//     }

//     $scope.submit = function (key, value, index) {
//         var key2 = {};
//         key2[key] = value;
//         key2["indexe"] = index;
//         console.log(key2, index);
//         $http.post("http://127.0.0.1:8080/update/home", key2).then(function (response) {
//             console.log(response);
//             $scope.update();
//         });
//     }

//     $scope.remove = function (index) {
//         $http.post("http://127.0.0.1:8080/update/home/remove", { "indexe": index }).then(function (response) {
//             console.log(response);
//             $scope.update();
//         });
//     }

//     $scope.addInner = function () {
//         $scope.home.push({ "New Value": "Value" });
//         //$scope.update();
//     };

//     $scope.update();
// });
// ///////////////////////////////////////////////////////

// ////////////////////////Dashboard-User////////////////////////
// app.controller("dashboardUserController", ['$scope', '$rootScope', '$http', '$location', '$localStorage', '$window', '$routeParams', 'factory', function ($scope, $rootScope, $http, $location, $localStorage, $window, $routeParams, factory) {
//     $scope.dash = {};
//     $scope.success = false;
//     var tempDict = JSON.parse($window.localStorage.getItem("user"))
//     $scope.update = function () {
//         $scope.dash = {
//             "firstname": tempDict.firstname,
//             "lastname": tempDict.lastname,
//             "username": tempDict.username,
//             "email": tempDict.email
//         };
//     }

//     $scope.submit = function () {
//         tempDict = $scope.dash;
//         $http({
//             method: 'POST',
//             url: 'http://127.0.0.1:8080/user_api/changepass',
//             data: {
//                 username: tempDict.username,
//                 firstname: tempDict.firstname,
//                 lastname: tempDict.lastname,
//                 email: tempDict.email,
//                 password: tempDict.password,
//                 newpassword: tempDict.newpassword
//             }
//         })
//             .then(function (response) {
//                 if (response.status == 200) {
//                     $scope.success = true;
//                     $window.localStorage.setItem("user", JSON.stringify({
//                         "username": response.data.username,
//                         "firstname": response.data.firstname,
//                         "lastname": response.data.lastname,
//                         "email": response.data.email
//                     }));

//                     if (response.data.status == "OK") {
//                         console.log(response.data);
//                         $location.search({ redirectFrom: $location.path() });
//                         $location.path("/login");
//                     }
//                 } else {
//                     $scope.success = false;
//                     console.log("Incorrect Password");
//                     console.log(response.status);
//                     $location.search({ redirectFrom: $location.path() });
//                     $location.path("/login");
//                 }
//             },
//                 function (response) {
//                     if (response.status == 401) {
//                         $scope.success = false;
//                         console.log(response.status);
//                         $location.search({ redirectFrom: $location.path() });
//                         $location.path("/login");
//                     }
//                 });

//     }

//     $scope.update();
// }]);
// ///////////////////////////////////////////////////////


// app.controller("dashboardAdminController", ['$scope', '$rootScope', '$http', '$location', '$localStorage', '$window', '$routeParams', 'factory', function ($scope, $rootScope, $http, $location, $localStorage, $window, $routeParams, factory) {
//     $scope.dash = {};
//     $scope.success = false;
//     var tempDict = JSON.parse($window.localStorage.getItem("user"))
//     $scope.update = function () {
//         $scope.dash = {
//             "firstname": tempDict.firstname,
//             "lastname": tempDict.lastname,
//             "username": tempDict.username,
//             "email": tempDict.email
//         };
//     }

//     $scope.submit = function () {
//         tempDict = $scope.dash;
//         $http({
//             method: 'POST',
//             url: 'http://127.0.0.1:8080/user_api/changepass',
//             data: {
//                 username: tempDict.username,
//                 firstname: tempDict.firstname,
//                 lastname: tempDict.lastname,
//                 email: tempDict.email,
//                 password: tempDict.password,
//                 newpassword: tempDict.newpassword
//             }
//         })
//             .then(function (response) {
//                 if (response.status == 200) {
//                     $scope.success = true;
//                     $window.localStorage.setItem("user", JSON.stringify({
//                         "username": response.data.username,
//                         "firstname": response.data.firstname,
//                         "lastname": response.data.lastname,
//                         "email": response.data.email
//                     }));

//                     if (response.data.status == "OK") {
//                         console.log(response.data);
//                         $location.search({ redirectFrom: $location.path() });
//                         $location.path("/login");
//                     }
//                 } else {
//                     $scope.success = false;
//                     console.log("Incorrect Password");
//                     console.log(response.status);
//                     $location.search({ redirectFrom: $location.path() });
//                     $location.path("/login");
//                 }
//             },
//                 function (response) {
//                     if (response.status == 401) {
//                         $scope.success = false;
//                         console.log(response.status);
//                         $location.search({ redirectFrom: $location.path() });
//                         $location.path("/login");
//                     }
//                 });

//     }

//     $scope.update();
// }]);

// ////////////////////////Menu////////////////////////
// app.controller('menuController', ['$scope', '$http', '$location', '$routeParams', '$anchorScroll', '$timeout', function ($scope, $http, $location, $routeParams, $anchorScroll, $timeout) {

//     $scope.addtoMenu = function (typedish, tempItem) {
//         $scope.menu[typedish].push({
//             "name": tempItem.name,
//             "description": tempItem.description,
//             "price": tempItem.price
//         });
//     };

//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/menu").then(function (response) {
//             console.log(response.status);
//             if (response.status == 200) {
//                 var tempDict = response.data;
//                 console.log(tempDict);
//                 console.log("hello");
//                 $scope.menu = { "Drinks": [], "Mains": [], "Soups and Appetizers": [], "Dessert": [] };

//                 for (x in tempDict) {
//                     if (tempDict[x].type === "Drinks") {
//                         $scope.addtoMenu("Drinks", tempDict[x]);
//                     } else if (tempDict[x].type === "Main") {
//                         $scope.addtoMenu("Mains", tempDict[x]);
//                     } else if (tempDict[x].type === "Dessert") {
//                         $scope.addtoMenu("Dessert", tempDict[x]);
//                     } else {
//                         $scope.addtoMenu("Soups and Appetizers", tempDict[x]);
//                     }
//                 }
//                 console.log($scope.menu);
//             }
//         });
//     };


//     $scope.scrollToHash = function (value) {
//         $timeout(function () {
//             console.log(value);
//             $location.hash(value);
//             $anchorScroll();
//         });
//     }
//     $scope.update();
// }]);
// ///////////////////////////////////////////////////////


// app.controller('menuAdminController', function ($scope, $http, $location, $routeParams) {

//     $scope.addtoMenu = function (typedish, tempItem) {

//         if ($scope.menu[typedish] === [] || $scope.menu[typedish] == null) {
//             $scope.menu[typedish] = [];
//         }

//         $scope.menu[typedish].push({
//             "name": tempItem.name,
//             "description": tempItem.description,
//             "price": tempItem.price
//         });
//     };

//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/menu").then(function (response) {
//             console.log(response.status);
//             if (response.status == 200) {
//                 var tempDict = response.data;
//                 console.log(tempDict);
//                 console.log("hello");
//                 $scope.menu = {};

//                 for (x in tempDict) {
//                     console.log(tempDict[x].type);
//                     $scope.addtoMenu(tempDict[x].type, tempDict[x]);
//                 }
//                 console.log($scope.menu);
//             }
//         },

//             function (response) {
//                 console.log(response.status);
//                 $location.search({ redirectFrom: $location.path() });
//                 $location.path("/login");
//             }
//         );
//     };


//     $scope.addInner = function (x) {
//         $scope.menu[x].push({
//             "name": "Name",
//             "description": "Description",
//             "price": 0
//         });
//     }

//     $scope.addOuter = function (x) {
//         $scope.menu[x] = [];
//     }

//     $scope.remove = function (x, y) {
//         let z;
//         $http({
//             method: "POST",
//             url: "http://127.0.0.1:8080/update/menu/remove/",
//             data: { "title": x, "index": y }
//         })
//             .then(function (response) {
//                 $scope.update();
//             });
//     }

//     $scope.removeAll = function (x, y) {
//         let z;
//         $http({
//             method: "POST",
//             url: "http://127.0.0.1:8080/update/menu/removeAll/",
//             data: { "title": x }
//         })
//             .then(function (response) {
//                 $scope.update();
//             });
//     }

//     $scope.submit = function (x, y, z) {
//         $http({
//             method: "POST",
//             url: "http://127.0.0.1:8080/update/menu/",
//             data: { "title": x, "value": y, "index": z }
//         })
//             .then(function (response) {
//                 $scope.update();
//             });
//         $scope.menu[x].splice(y, 1);
//     }

//     $scope.update();
// });
// ////////////////////////Contact////////////////////////
// app.controller('contactController', function ($scope, $http) {
//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/contact").then(function (response) {
//             var tempDict = response.data;
//             console.log(tempDict);
//             $scope.contact = {};
//             console.log(tempDict);
//             $scope.contact = {
//                 "name": tempDict.name,
//                 "address": tempDict.address,
//                 "city": tempDict.city,
//                 "province": tempDict.province,
//                 "postal": tempDict.postal,
//                 "hours": tempDict.hours,
//                 "phone": tempDict.phone
//             };
//         });
//     };
//     $scope.update();
// });
// ////////////////////////////////////////////////

// app.controller('dailyController', function ($scope, $http, $location, $routeParams) {

//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/daily").then(function (response) {
//             console.log(response.status);
//             if (response.status == 200) {
//                 var tempDict = response.data;
//                 console.log(tempDict);
//                 console.log("hello");
//                 $scope.daily = {};
//                 for (x in tempDict) {
//                     if ($scope.daily[tempDict[x].type] === [] || $scope.daily[tempDict[x].type] == null) {
//                         $scope.daily[tempDict[x].type] = [];
//                     }

//                     $scope.daily[tempDict[x].type].push({
//                         "day": tempDict[x].day,
//                         "special": tempDict[x].special,
//                     });
//                     console.log($scope.daily);
//                 }
//             }
//         });
//     };
//     $scope.update();
// });
// //////////////////////////////////////////////////////////////


// app.controller('dailyAdminController', function ($scope, $http, $location, $routeParams) {

//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/daily").then(function (response) {
//             console.log(response.status);
//             if (response.status == 200) {
//                 var tempDict = response.data;
//                 console.log(tempDict);
//                 console.log("hello");
//                 $scope.daily = {};
//                 for (x in tempDict) {
//                     if ($scope.daily[tempDict[x].type] === [] || $scope.daily[tempDict[x].type] == null) {
//                         $scope.daily[tempDict[x].type] = [];
//                     }

//                     $scope.daily[tempDict[x].type].push({
//                         "day": tempDict[x].day,
//                         "special": tempDict[x].special,
//                     });
//                     console.log($scope.daily);
//                 }
//             }
//         });
//     };

//     $scope.removeSec = function(value, type) {
//         $http({
//             method: "POST",
//             url:"http://127.0.0.1:8080/update/daily/removesec/",
//             data: {day:value, type:type}
//         })
//         .then(function(response){
//             $scope.update();
//         });
//     };

//     $scope.remove = function(value, content, type, index) {
//         console.log({day:value, content:content, type:type, index:index});
//         $http({
//             method: "POST",
//             url:"http://127.0.0.1:8080/update/daily/remove/",
//             data: {day:value, content:content, type:type, index:index}
//         })
//         .then(function(response){
//             $scope.update();
//         });
//     };

//     $scope.submit = function (type, day, content, pindex, index) {
//         $http({
//             method: "POST",
//             url:"http://127.0.0.1:8080/update/daily/",
//             data: {type:type, day:day, content:content, pindex:pindex, index:index}
//         })
//         .then(function(response){
//             $scope.update();
//         });
//     };

//     $scope.addInner = function (value, day, index) {
//         console.log(value, day);
//         $scope.daily[value][index].special.push("");
//     };
//     $scope.update();
// });

// ////////////////////////Review////////////////////////
// app.controller('reviewController', ['$scope', '$http', '$location', function ($scope, $http, $location) {
//     $scope.orderDate = function (value) {
//         return new Date(value.date);
//     };

//     $scope.show = false;

//     $scope.showForm = function () {
//         if ($scope.show) {
//             $scope.show = false;
//         } else {
//             $scope.show = true;
//         }
//     };
//     $scope.submit = function () {
//         var months = ["January", "February", "March", "April", "May", "June",
//             "July", "August", "September", "October", "November", "December"];
//         console.log(this.date);
//         var stringDate = months[this.date.getMonth()] + " " + this.date.getDate() + ", " + this.date.getFullYear();
//         var newDict = {
//             "quote": this.quote,
//             "name": this.name,
//             "date": stringDate
//         };
//         $http.post('http://127.0.0.1:8080/update/review/', newDict).then(function () {
//             $scope.update();
//         },

//             function (response) {
//                 console.log(response.status);
//                 $location.search({ redirectFrom: $location.path() });
//                 $location.path("/login");
//             }
//         );
//         $scope.show = false;
//         $scope.update();
//     };

//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/review/").then(function (response) {
//             console.log(response.data);
//             $scope.review = [];
//             var tempDict = response.data;
//             for (x in tempDict) {
//                 $scope.review.push(tempDict[x]);
//             }
//         });
//     };

//     $scope.update();


// }]);
// ////////////////////////////////////////////////


// ////////////////////////Review-Admin////////////////////////
// app.controller('reviewAdminController', function ($scope, $http, factory) {
//     $scope.orderDate = function (value) {
//         return new Date(value.date);
//     };

//     $scope.update = function () {
//         $http.get("http://127.0.0.1:8080/update/review/").then(function (response) {
//             console.log(response.data);
//             $scope.review = [];
//             var tempDict = response.data;
//             for (x in tempDict) {
//                 $scope.review.push(tempDict[x]);
//             }
//         });
//     };

//     $scope.remove = function (value) {
//         $http.post("http://127.0.0.1:8080/update/review/remove/", { "value": value }, function () { $scope.update(); });
//         console.log(value);
//         $scope.update();
//     };
//     $scope.update();
// });
// ////////////////////////////////////////////////


// // app.controller('loginController', function ($scope) {

// // });

// app.controller('mainController', ['$scope', '$rootScope', '$window', '$localStorage', '$http', '$location', function ($scope, $rootScope, $window, $localStorage, $http, $location) {
//     $rootScope.loginhide = false;

//     $scope.scrollTo = function (hash) {
//         $location.hash(hash);
//     };

//     $scope.checkLogin = function () {
//         try {
//             if (JSON.parse($window.localStorage.getItem("user")).token) {
//                 $rootScope.loginhide = true;
//                 $http.defaults.headers.common.authorization = JSON.parse($window.localStorage.getItem("user")).token;
//                 console.log(JSON.parse($window.localStorage.getItem("user")).token);
//             } else {
//                 $rootScope.loginhide = false;
//                 //$location.path('/home');
//             }
//         } catch (error) {
//             console.log(error);
//             $window.localStorage.setItem("user", "{}");
//             $rootScope.loginhide = false;
//             $http.defaults.headers.common.authorization = '';
//             $location.path('/home');
//         }

//     };


//     $scope.logout = function () {
//         $window.localStorage.removeItem("user");
//         // $http.defaults.headers.common.authorization = '';
//         $rootScope.loginhide = false;
//         $scope.checkLogin();
//     };

//     $scope.checkLogin();
//     // console.log("hello");
//     $scope.windowWidth = $window.innerWidth;
//     $scope.windowHeight = $window.innerHeight;
//     angular.element($window).bind('resize', function () {
//         $scope.windowWidth = $window.innerWidth;
//         $scope.$apply();
//     });
//     console.log($scope.windowHeight);
//     angular.element(document.querySelector('.bigimage')).css('padding', (($scope.windowHeight / 2 - 125).toString() + "px").toString());
//     // angular.element(document.querySelector('.inneribody')).css('width', (($scope.windowWidth).toString() + "px").toString());
//     // angular.element(document.querySelector('.inneribody')).css('height', (($scope.windowHeight).toString() + "px").toString());

//     angular.forEach(document.getElementsByClassName('inneribody'), function (value, key) {
//         angular.element(value).css('width', (($scope.windowWidth).toString() + "px").toString());
//         angular.element(value).css('height', (($scope.windowHeight).toString() + "px").toString());
//     });


//     $scope.chooseRedirect = function () {
//         if (JSON.parse($window.localStorage.getItem("user")).permissions == "admin") {
//             $location.path("/dashboard-admin");
//         } else {
//             $location.path("/dashboard-user");
//         }
//     }
// }]);


app.controller("mainController", function ($scope) {
    console.log("hello");
});

app.controller("homeController", function ($scope) {
    console.log("hello");
});