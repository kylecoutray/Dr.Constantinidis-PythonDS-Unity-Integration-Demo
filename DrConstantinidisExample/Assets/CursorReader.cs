using System;
using System.IO;
using UnityEngine;

public class CursorReader : MonoBehaviour
{
    private string filePath = "D:/suchaklutch/Dr.Constantinidis-PythonDS-Unity-Integration-Demo/DrConstantinidisExample/cursor_data.txt";

    void Update()
    {
        try
        {
            // Check if the file exists
            if (File.Exists(filePath))
            {
                // Open file in read-only mode
                using (FileStream stream = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))
                {
                    using (StreamReader reader = new StreamReader(stream))
                    {
                        // Read the latest line
                        string data = reader.ReadToEnd().Trim();

                        // Log the data to the Unity console
                        if (!string.IsNullOrEmpty(data))
                        {
                            Debug.Log("Cursor Position from Python: " + data);
                        }
                    }
                }
            }
            else
            {
                Debug.LogWarning("File not found: " + filePath);
            }
        }
        catch (Exception ex)
        {
            Debug.LogError("Error reading file: " + ex.Message);
        }
    }
}
