use actix_web::{get, App, HttpResponse, HttpServer, Responder};
use chrono::Datelike;

#[get("/")]
async fn index() -> impl Responder {
    let current_year = chrono::Utc::now().year();
    let html = format!(
        r#"<!DOCTYPE html>
        <html lang="id">
        <head>
            <meta charset="UTF-8">
            <title>IndoInves - Platform Pintar Investasi & Keuangan</title>
            <style>
                body {{ font-family: system-ui, sans-serif; background-color: #f8fafc; color: #1e293b; display: flex; min-height: 100vh; justify-content: center; align-items: center; text-align: center; margin: 0; }}
                .container {{ max-width: 600px; background: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
                img.logo {{ width: 100px; height: 100px; border-radius: 50%; margin-bottom: 20px; }}
                h1 {{ color: #0f172a; font-size: 24px; margin-bottom: 10px; }}
                p {{ color: #64748b; margin-bottom: 25px; }}
                .btn {{ background-color: #2563eb; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: 600; display: inline-block; }}
                footer {{ margin-top: 30px; font-size: 14px; color: #94a3b8; }}
            </style>
        </head>
        <body>
            <div class="container">
                <img src="https://indoinves.github.io/img/indoinves.png" class="logo" alt="Logo">
                <h1>Selamat Datang di IndoInves</h1>
                <p>Platform pintar investasi, keuangan, dan kumpulan tools finansial modern.</p>
                <div>
                    <a href="https://indoinves.github.io/" class="btn">Buka Website Utama</a>
                </div>
                <footer>&copy; {} IndoInves. All rights reserved.</footer>
            </div>
        </body>
        </html>"#,
        current_year
    );

    HttpResponse::Ok().content_type("text/html; charset=utf-8").body(html)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("Server berjalan di http://localhost:8080");
    HttpServer::new(|| {
        App::new().service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
