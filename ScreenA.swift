import SwiftUI
import PythonKit



struct ScreenA: View {
    @State private var selectedOption1 = 0
    @State private var selectedOption2 = 0
    @State private var predictionResult = ""
    let options1 = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", "Crystal Palace", "Everton",
                    "Fulham", "Leeds", "Leicester", "Liverpool", "Man City", "Man United", "Newcastle", "Nott'm Forest", "Southampton",
                    "Tottenham", "West Ham", "Wolves"]
    
    let options2 = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", "Crystal Palace", "Everton",
                    "Fulham", "Leeds", "Leicester", "Liverpool", "Man City", "Man United", "Newcastle", "Nott'm Forest", "Southampton",
                    "Tottenham", "West Ham", "Wolves"]

    var body: some View {
        ZStack{
            Image("Image1")
            HStack{
                VStack {
                    Text("Select Home Team:").font(.title).fontWeight(.medium).bold()
                    
                    Picker("Options 1", selection: $selectedOption1) {
                        ForEach(0..<options1.count, id: \.self) { index in
                            Text(options1[index]).tag(index)
                        }
                    }
                    
                    .pickerStyle(MenuPickerStyle())
                    Text("Home Team: \(options1[selectedOption1])")
                        .font(.title)
                    
                    Text("Select Away Team:").font(.title).fontWeight(.medium).bold()
                    Picker("Options2", selection: $selectedOption2) {
                        ForEach(0..<options2.count, id: \.self) { index in
                            Text(options2[index]).tag(index)
                        }
                    }
                    
                    .pickerStyle(MenuPickerStyle()) // This creates a dropdown menu style.
                    Text("Away Team: \(options2[selectedOption2])")
                        .font(.title)
                
                    Button("Predict Winner") {
                        let homeTeam = options1[selectedOption1]
                        let awayTeam = options2[selectedOption2]
                        runPythonScript(homeTeam: homeTeam, awayTeam: awayTeam)
                        
                    }
                
                    Text("Prediction Result:")
                            Text(predictionResult)
                }
            }
        }
    }

    func runPythonScript(homeTeam: String, awayTeam: String) {
        let sys = Python.import("sys")
        let pythonScript = Python.open("predict.py")

        // Redirect Python's stdout to a file
        let outputFile = "output.txt"
        Python.sys.stdout = Python.open(outputFile, mode: "w")

        sys.argv = [PythonObject(homeTeam), PythonObject(awayTeam)]

        Python.exec(pythonScript)

        // Close the output file
        Python.sys.stdout.close()

        // Read the content of the output file
        if let outputText = try? String(contentsOfFile: outputFile) {
            predictionResult = outputText
        }
    }
}

struct ScreenA_Previews: PreviewProvider{
    static var previews: some View{
        ScreenA()
    }
}

struct Previews_ScreenA_LibraryContent: LibraryContentProvider {
    var views: [LibraryItem] {
        LibraryItem(/*@START_MENU_TOKEN@*/Text("Hello, World!")/*@END_MENU_TOKEN@*/)
    }
}
