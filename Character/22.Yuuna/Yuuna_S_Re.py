import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] < 4)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
   
         f.distance[cp] = 50;
         
         f.Table_Cos(cp, 45 * f.count[cp], f.distance[cp]);
         f.Table_Sin(cp, 45 * f.count[cp], f.distance[cp]);
        
         f.SquareShape(cp, 1, "Protoss Dark Templar", f.CosAngle[cp], f.SinAngle[cp]);
         f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
         f.SkillUnit(cp, 1, "40 + 1n Mojo");
         f.MoveLoc(f.heroID[cp], cp, -f.CosAngle[cp], -f.SinAngle[cp]);
         f.SkillUnit(cp, 1, "40 + 1n Mojo");

         KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         
         f.SkillWait(cp, 160);
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         f.Table_Cos(cp, 0, f.distance[cp]);
         f.Table_Sin(cp, 0, f.distance[cp]);
            
         f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);

         f.Table_Cos(cp, 45, f.distance[cp]);
         f.Table_Sin(cp, 45, f.distance[cp]);
            
       f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);

         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

         f.SkillWait(cp, 50);
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 5)
      {
         f.distance[cp] = 75;

         f.Table_Cos(cp, 0, f.distance[cp]);
         f.Table_Sin(cp, 0, f.distance[cp]);
            
         f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);

         f.Table_Cos(cp, 45, f.distance[cp]);
         f.Table_Sin(cp, 45, f.distance[cp]);
            
         f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
      
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

         f.SkillWait(cp, 50);
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 6)
      {
         f.distance[cp] = 50;
         f.Table_Cos(cp, 0, f.distance[cp]);
         f.Table_Sin(cp, 0, f.distance[cp]);
            
         f.SquareShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);

         f.Table_Cos(cp, 45, f.distance[cp]);
         f.Table_Sin(cp, 45, f.distance[cp]);
            
         f.SquareShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

         f.SkillWait(cp, 160);
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 7)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         f.SkillWait(cp, 80);
         f.count[cp] += 1;
      }
      else if (f.count[cp] == 8)
      {
         f.SkillEnd(cp);
      }
   }
}