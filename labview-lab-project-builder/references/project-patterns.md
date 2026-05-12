# Project Patterns

## Minimal `.lvproj`

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="25008000">
  <Property Name="NI.LV.All.SaveVersion" Type="Str">Editor version</Property>
  <Property Name="NI.LV.All.SourceOnly" Type="Bool">false</Property>
  <Property Name="NI.Project.Description" Type="Str">...</Property>
  <Item Name="My Computer" Type="My Computer">
    <Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
    <Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
    <Property Name="server.tcp.enabled" Type="Bool">false</Property>
    <Property Name="server.tcp.port" Type="Int">0</Property>
    <Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
    <Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
    <Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
    <Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
    <Property Name="specify.custom.address" Type="Bool">false</Property>
    <Item Name="Main VI" Type="Folder">
      <Item Name="主程序.vi" Type="VI" URL="../Main.vi"/>
    </Item>
    <Item Name="Dependencies" Type="Dependencies"/>
    <Item Name="Build Specifications" Type="Build"/>
  </Item>
</Project>
```

## `.aliases`

```ini
[My Computer]
My Computer = "localhost"

[ProjectWindow_Data]
ProjectExplorer.ClassicPosition[String] = "50,50,950,700"
```

## XML Encoding

Write `.lvproj` with UTF-8 and XML escaping. Validate by parsing as XML before opening in LabVIEW.

## Document Items

Use `Type="Document"` for `.md`, `.docx`, `.png`, `.csv`, `.html`, and `.py` support files that should appear in the project tree.
