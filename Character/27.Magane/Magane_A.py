import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {        
            f.Table_Sin(cp, 45, 50);
            f.Table_Cos(cp, 45, 50);

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 22, 125);
            f.Table_Cos(cp, 22, 125);

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {        
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.Table_Sin(cp, 45, 50);
            f.Table_Cos(cp, 45, 50);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 22, 125);
            f.Table_Cos(cp, 22, 125);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {        
            f.Table_Sin(cp, 90, 50);
            f.Table_Cos(cp, 90, 50);

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 125);
            f.Table_Cos(cp, 67, 125);

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {        
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.Table_Sin(cp, 90, 50);
            f.Table_Cos(cp, 90, 50);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 125);
            f.Table_Cos(cp, 67, 125);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 2)
         {       
            f.Table_Sin(cp, 90 * f.loop[cp] + 45, f.loop[cp] * 75 + 75);
            f.Table_Cos(cp, 90 * f.loop[cp] + 45, f.loop[cp] * 75 + 75);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.Table_Sin(cp, 90 * f.loop[cp], f.loop[cp] * 75 + 75);
            f.Table_Cos(cp, 90 * f.loop[cp], f.loop[cp] * 75 + 75);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.Table_Sin(cp, 90 * f.loop[cp] + 45, 150);
            f.Table_Cos(cp, 90 * f.loop[cp] + 45, 150);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 90 * f.loop[cp], 150);
            f.Table_Cos(cp, 90 * f.loop[cp], 150);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            var x = 32;
            var y = 32;

            f.SquareShape(cp, 1, "40 + 1n Wraith", x, y);
            f.DoubleShape(cp, 1, "60 + 1n Archon", x, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", -x, y);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            var x = 32;
            var y = 32;

            f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
            f.DoubleShape(cp, 1, "60 + 1n Archon", -x, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);


         f.SkillEnd(cp);
      }
   }
}