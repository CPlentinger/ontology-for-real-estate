using System.Xml;
using System.Xml.Schema;

namespace xsd_inference
{
    class XsdInference
    {
        static void Main(string[] args)
        {
            // Get all files in the XML directory
            string[] files = Directory.GetFiles("XML", "*.xml");
            
            XmlWriterSettings settings = new XmlWriterSettings
            {
                Indent = true,
                IndentChars = "  ",
                NewLineOnAttributes = false,
                OmitXmlDeclaration = false
            };
            
            foreach (var file in files)
            {
                XmlReader reader = XmlReader.Create(file);
                XmlSchemaInference inference = new XmlSchemaInference();
                XmlSchemaSet schemaSet = inference.InferSchema(reader);

                int index = 0;
                int numberOfSchemas = schemaSet.Schemas().Count;
                foreach (XmlSchema schema in schemaSet.Schemas())
                {
                    string outputPath;
                    if (numberOfSchemas == 1)
                    {
                        outputPath = $"XSD/{Path.GetFileNameWithoutExtension(file)}/result.xsd";
                    }
                    else
                    {
                        outputPath = $"XSD/{Path.GetFileNameWithoutExtension(file)}/result{index + 1}.xsd";
                    }
                    
                    Directory.CreateDirectory(Path.GetDirectoryName(outputPath)!);
                    
                    using XmlWriter writer = XmlWriter.Create(outputPath, settings);
                    schema.Write(writer);
                    index++;
                }
            }
        }
    }
}