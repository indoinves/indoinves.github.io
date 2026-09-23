import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack {
            // Background color
            Color(UIColor(.sRGB, red: 0.97, green: 0.98, blue: 0.99, opacity: 1.0))
                .ignoresSafeArea()
            
            VStack(spacing: 20) {
                // Logo Image
                AsyncImage(url: URL(string: "https://indoinves.github.io/img/indoinves.png")) { phase in
                    switch phase {
                    case .empty:
                        ProgressView()
                            .frame(width: 100, height: 100)
                    case .success(let image):
                        image
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                            .frame(width: 100, height: 100)
                            .clipShape(Circle())
                    case .failure(_):
                        Image(systemName: "photo")
                            .font(.system(size: 40))
                            .foregroundColor(.gray)
                            .frame(width: 100, height: 100)
                            .background(Color.gray.opacity(0.2))
                            .clipShape(Circle())
                    @unknown default:
                        EmptyView()
                    }
                }
                .shadow(radius: 4)
                
                // Title
                Text("Selamat Datang di IndoInves")
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundColor(Color(UIColor(.sRGB, red: 0.06, green: 0.09, blue: 0.16, opacity: 1.0)))
                    .multilineTextAlignment(.center)
                
                // Description
                Text("Platform pintar investasi, keuangan, dan kumpulan tools finansial modern untuk membantu masa depan finansial Anda.")
                    .font(.subheadline)
                    .foregroundColor(Color(UIColor(.sRGB, red: 0.39, green: 0.45, blue: 0.55, opacity: 1.0)))
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 10)
                
                // Buttons
                VStack(spacing: 12) {
                    Link(destination: URL(string: "https://indoinves.github.io/")!) {
                        Text("Buka Website Utama")
                            .font(.headline)
                            .foregroundColor(.white)
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(Color.blue)
                            .cornerRadius(8)
                    }
                    
                    Link(destination: URL(string: "https://indoinves.github.io/tools/investasi.html")!) {
                        Text("Jelajahi Tools")
                            .font(.headline)
                            .foregroundColor(Color(UIColor(.sRGB, red: 0.28, green: 0.33, blue: 0.41, opacity: 1.0)))
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(Color(UIColor(.sRGB, red: 0.88, green: 0.91, blue: 0.94, opacity: 1.0)))
                            .cornerRadius(8)
                    }
                }
                .padding(.top, 10)
                
                Spacer()
                    .frame(height: 20)
                
                // Footer
                Text("© 2026 IndoInves. All rights reserved.")
                    .font(.footnote)
                    .foregroundColor(Color(UIColor(.sRGB, red: 0.58, green: 0.64, blue: 0.72, opacity: 1.0)))
            }
            .padding(30)
            .background(Color.white)
            .cornerRadius(16)
            .shadow(color: Color.black.opacity(0.08), radius: 8, x: 0, y: 4)
            .padding(.horizontal, 20)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
