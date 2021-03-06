import Function as f;

function main(cp)
{
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 8)
         {             
            if (f.loop[cp] == 0)
            {
               f.Table_Sin(cp, 22, 50);
               f.Table_Cos(cp, 22, 50);

               f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);

               f.Table_Sin(cp, 67, 100);
               f.Table_Cos(cp, 67, 100);

               f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);

            }
            else if (f.loop[cp] == 2)
            {
               RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

               f.Table_Sin(cp, 22, 100);
               f.Table_Cos(cp, 22, 100);

               f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);

               f.Table_Sin(cp, 67, 150);
               f.Table_Cos(cp, 67, 150);

               f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
            }
            else if (f.loop[cp] == 4)
            {
               RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

               f.Table_Sin(cp, 22, 50);
               f.Table_Cos(cp, 22, 50);

               f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);

               f.Table_Sin(cp, 67, 100);
               f.Table_Cos(cp, 67, 100);

               f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);

               f.Table_Sin(cp, 22, 100);
               f.Table_Cos(cp, 22, 100);

               f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);

               f.Table_Sin(cp, 67, 150);
               f.Table_Cos(cp, 67, 150);

               f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);

               f.Table_Sin(cp, 22, 150);
               f.Table_Cos(cp, 22, 150);

               f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);

               KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
               KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            }

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");

            f.SquareShape(cp, 1, "40 + 1n Guardian", 160 - 40 * f.loop[cp], 160);
            f.SquareShape(cp, 1, "60 + 1n Archon", 160 - 40 * f.loop[cp], 160);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);


            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.EdgeShape(cp, 1, "40 + 1n Ghost", 0, 3, 160);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);

            f.EdgeShape(cp, 1, "40 + 1n Guardian", 45, 7, 160);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 7, 160);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 3)
         {             
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.DotShape(cp, 8, "Bengalaas (Jungle)", 0, 0);
            f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);

            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Guardian", 45, 7, 160);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 7, 160);

            f.SquareShape(cp, 1, " Creep. Dunkelheit", 80, 80);
            f.SquareShape(cp, 7, "60 + 1n High Templar", 80, 80);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Wraith", 45, 7, 160);
            f.EdgeShape(cp, 1, " Creep. Dunkelheit", 45, 7, 160);
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }

         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 7, 160);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 7, 160);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         f.SkillEnd(cp);
      }
   }
}