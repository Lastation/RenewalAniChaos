import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

         if (f.loop[cp] % 2 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.Table_Sin(cp, 22 * (f.loop[cp] / 2), 150); 
            f.Table_Cos(cp, 22 * (f.loop[cp] / 2), 150);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.Table_Sin(cp, 22 * (f.loop[cp] / 2) + 45, 150); 
            f.Table_Cos(cp, 22 * (f.loop[cp] / 2) + 45, 150);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         f.DotShape(cp, 1, "40 + 1n Mutalisk", 0, 0);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, "Anywhere");

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

         if (f.loop[cp] % 2 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.Table_Sin(cp, 22 * (f.loop[cp] / 2), 150); 
            f.Table_Cos(cp, 22 * (f.loop[cp] / 2), 150);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.Table_Sin(cp, 22 * (f.loop[cp] / 2) + 45, 150); 
            f.Table_Cos(cp, 22 * (f.loop[cp] / 2) + 45, 150);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, "Anywhere");

            f.Table_Sin(cp, 22 * (f.loop[cp] / 2), 50); 
            f.Table_Cos(cp, 22 * (f.loop[cp] / 2), 50);

            f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}