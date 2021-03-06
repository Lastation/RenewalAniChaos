import Function as f;

function main(cp)
{
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 3)
         {             
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            f.LineShape(cp, 1, "40 + 1n Mutalisk", 45 * f.loop[cp], 9, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 45 * f.loop[cp], 9, 50, 75);
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 45 * f.loop[cp] + 180, 9, 50, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 45 * f.loop[cp], 7, 75, 0);
            f.LineShape(cp, 1, "60 + 1n Archon", 45 * f.loop[cp], 7, 75, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 45 * f.loop[cp] + 180, 7, 75, 75);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 45 * f.loop[cp], 9, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 45 * f.loop[cp], 9, 50, 75);
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 45 * f.loop[cp] + 180, 9, 50, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 45 * f.loop[cp], 7, 75, 0);
            f.LineShape(cp, 1, "60 + 1n Archon", 45 * f.loop[cp], 7, 75, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 45 * f.loop[cp] + 180, 7, 75, 75);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 8)
         {             
            if (f.loop[cp] == 0)
            {
               f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45, 7, 75, 0);
               f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45, 7, 75, 75);
               f.LineShape(cp, 1, "50 + 1n Battlecruiser", 225, 7, 75, 75);
               f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 7, 75, 0);
               f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 7, 75, 75);
               f.LineShape(cp, 1, " Unit. Hoffnung 25000", 225, 7, 75, 75);

               KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
            }
            if (f.loop[cp] % 2 == 0)
            {
               RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

               f.SquareShape(cp, 1, "40 + 1n Wraith", 160 - 40 * f.loop[cp], 160);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

               f.Table_Sin(cp, 22 + 45 * f.loop[cp], 50 + 25 * f.loop[cp]);
               f.Table_Cos(cp, 22 + 45 * f.loop[cp], 50 + 25 * f.loop[cp]);

               f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            }
            else if (f.loop[cp] % 2 == 1)
            {
               f.SquareShape(cp, 1, "40 + 1n Mojo", 160 - 40 * f.loop[cp], 160);
               KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

               f.Table_Sin(cp, 45 * f.loop[cp], 50 + 25 * f.loop[cp]);
               f.Table_Cos(cp, 45 * f.loop[cp], 50 + 25 * f.loop[cp]);

               f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            }

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 160 - 40 * f.loop[cp], 160);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Mutalisk", 45, 7, 160);
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 7, 160);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Ghost", 45, 5, 200);

            f.EdgeShape(cp, 1, "40 + 1n Wraith", 45, 7, 160);
            f.EdgeShape(cp, 1, "40 + 1n Drone", 45, 7, 160);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 400);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {         
            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 45, 7, 50, 75);
            f.LineShape(cp, 1, "Protoss Dark Archon", 225, 7, 50, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 75);
            f.LineShape(cp, 1, "40 + 1n Wraith", 225, 5, 75, 75);
            f.LineShape(cp, 1, "50 + 1n Tank", 45, 7, 50, 150);
            f.LineShape(cp, 1, "50 + 1n Tank", 225, 7, 50, 150);

            f.DoubleShape(cp, 1, "40 + 1n Mutalisk", 50, 50);
            f.DoubleShape(cp, 1, "40 + 1n Mutalisk", 125, 125);

            f.DoubleShape(cp, 1, "60 + 1n High Templar", 50, 50);
            f.DoubleShape(cp, 1, "60 + 1n High Templar", 125, 125);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 5, 75, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 135, 7, 50, 75);
            f.LineShape(cp, 1, "Protoss Dark Archon", 315, 7, 50, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 5, 75, 75);
            f.LineShape(cp, 1, "40 + 1n Wraith", 315, 5, 75, 75);
            f.LineShape(cp, 1, "50 + 1n Tank", 135, 7, 50, 150);
            f.LineShape(cp, 1, "50 + 1n Tank", 315, 7, 50, 150);

            f.DoubleShape(cp, 1, "40 + 1n Mutalisk", -50, 50);
            f.DoubleShape(cp, 1, "40 + 1n Mutalisk", -125, 125);

            f.DoubleShape(cp, 1, "60 + 1n High Templar", -50, 50);
            f.DoubleShape(cp, 1, "60 + 1n High Templar", -125, 125);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 4)
         {             
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 180 - 45 * f.loop[cp], 9, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 180 - 45 * f.loop[cp], 9, 50, 75);
            f.LineShape(cp, 1, "40 + 1n Mutalisk", 180 - 45 * f.loop[cp] + 180, 9, 50, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 180 - 45 * f.loop[cp], 7, 75, 0);
            f.LineShape(cp, 1, "60 + 1n Archon", 180 - 45 * f.loop[cp], 7, 75, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 180 - 45 * f.loop[cp] + 180, 7, 75, 75);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 135, 7, 75, 0);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 135, 7, 75, 75);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 315, 7, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 7, 75, 0);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 7, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 315, 7, 75, 75);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 400);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

         f.SkillEnd(cp);
      }
   }
}