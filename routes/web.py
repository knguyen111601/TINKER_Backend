"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Post("/login", "AuthController@login").name("login"),
        Post("/signup", "AuthController@signup").name("signup"),
        Post("/logout", "AuthController@logout").name("logout")
    ], prefix="/auth"),

    # PC

    RouteGroup([
        Get("/", "PCOwnerController@get_user_pcs").name("get_pcs"),
        Post("/", "PCOwnerController@create").name("create"),
        Get("/@id", "PCOwnerController@show").name("show"),
        Put("/@id", "PCOwnerController@update").name("update"),
        Delete("/@id", "PCOwnerController@destroy").name("destroy")
    ], prefix="/pcs", middleware=["auth"]),

    # Case
    RouteGroup([
        Get("/", "CaseController@index").name("index"),
        Get("/@id", "CaseController@show").name("show")
    ], prefix="/cases", name="cases"),

    # Motherboard
    RouteGroup([
        Get("/", "MotherboardController@index").name("index"),
        Get("/@id", "MotherboardController@show").name("show")
    ], prefix="/motherboards", name="motherboards"),

    # Cooler
    RouteGroup([
        Get("/", "CoolerController@index").name("index"),
        Get("/@id", "CoolerController@show").name("show")
    ], prefix="/coolers", name="coolers"),

    # CPUs
    RouteGroup([
        Get("/", "CPUController@index").name("index"),
        Get("/@id", "CPUController@show").name("show")
    ], prefix="/cpus", name="cpus"),

    # RAM
    RouteGroup([
        Get("/", "RAMController@index").name("index"),
        Get("/@id", "RAMController@show").name("show")
    ], prefix="/ram", name="ram"),

    # GPU
    RouteGroup([
        Get("/", "GPUController@index").name("index"),
        Get("/@id", "GPUController@show").name("show")
    ], prefix="/gpus", name="gpus"),

    # PSU
    RouteGroup([
        Get("/", "PSUController@index").name("index"),
        Get("/@id", "PSUController@show").name("show")
    ], prefix="/psus", name="psus"),

    # Storage
    RouteGroup([
        Get("/", "StorageController@index").name("index"),
        Get("/@id", "StorageController@show").name("show")
    ], prefix="/storages", name="storages"),

        # Storage2
    RouteGroup([
        Get("/", "SecondStorageController@index").name("index"),
        Get("/@id", "SecondStorageController@show").name("show"),
        Delete("/@id", "SecondStorageController@destroy").name("destroy")
    ], prefix="/secondstorages", name="secondstorages"),

        # Storage3
    RouteGroup([
        Get("/", "ThirdStorageController@index").name("index"),
        Get("/@id", "ThirdStorageController@show").name("show")
    ], prefix="/thirdstorages", name="thirdstorages"),

        # Misc
    RouteGroup([
        Get("/", "MiscController@index").name("index"),
        Get("/@id", "MiscController@show").name("show")
    ], prefix="/miscs", name="miscs"),

        # Misc2
    RouteGroup([
        Get("/", "SecondMiscController@index").name("index"),
        Get("/@id", "SecondMiscController@show").name("show")
    ], prefix="/secondmiscs", name="secondmiscs"),

        # Misc3
    RouteGroup([
        Get("/", "ThirdMiscController@index").name("index"),
        Get("/@id", "ThirdMiscController@show").name("show")
    ], prefix="/thirdmiscs", name="thirdmiscs")
]