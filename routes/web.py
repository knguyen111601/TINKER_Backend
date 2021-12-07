"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Post("/login", "AuthController@login").name("login"),
        Post("/signup", "AuthController@signup").name("signup"),
        Post("/logout", "AuthController@logout").name("logout"),
    ], prefix="/auth"),

    RouteGroup([
        Get("/pc", "PCOwnerController@get_user_pcs").name("get_pcs"),
        Post("/pc", "PCOwnerController@create").name("create")
    ], prefix="/user", middleware=["auth"])


]