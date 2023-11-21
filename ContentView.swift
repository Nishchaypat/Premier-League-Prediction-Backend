//
//  ContentView.swift
//  POP
//
//  Created by Devansh Mohan Sinha on 10/15/23.
//


import SwiftUI
import UIKit

struct ContentView: View {
    var body: some View {
        NavigationView{
            
            ZStack{
                Image("Image1")
                VStack{
                    Spacer()
                    Image("POP")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: 200, height: 200.0)
                        .cornerRadius(20)
                        .shadow(radius: 20)
                    
                    Spacer()
                    
                    Button {
                        deal()
                    } label: { }
                    NavigationLink(destination: ScreenA()
                                   , label:{
                        
                        Image("Welcome")
                        
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 290)
                            .cornerRadius(15)
                            .shadow(radius: 20)
                    } )
                    
                    Spacer()
                }
            }
           
            }
        }

        func deal(){
            print("Welcome")
            
        }
        
    }

struct ContentView_Previews: PreviewProvider{
    static var previews: some View{
        ContentView()
    }
}
