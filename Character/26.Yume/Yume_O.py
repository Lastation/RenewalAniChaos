import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 2)
         {          
            f.DotShape(cp, 1, "40 + 1n Wraith", 0, 0);

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {                        
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 2)
         {          
            f.DotShape(cp, 1, "40 + 1n Wraith", 0, 0);

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {                        
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 4)
         {          
            f.DotShape(cp, 8, "Bengalaas (Jungle)", 0, 0);
            f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);

            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {                        
            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveLocation("26.Yume_Bozo", f.heroID[cp], cp, "Anywhere");

            if (cp < 3)
            {
               if (Bring(3, AtLeast, 1, f.heroID[3], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[3], 3, "Anywhere");
               }
               else if (Bring(4, AtLeast, 1, f.heroID[4], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[4], 4, "Anywhere");
               }
               else if (Bring(5, AtLeast, 1, f.heroID[5], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[5], 5, "Anywhere");
               }

            }
            else if (cp >= 3)
            {
               if (Bring(0, AtLeast, 1, f.heroID[0], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[0], 0, "Anywhere");
               }
               else if (Bring(1, AtLeast, 1, f.heroID[1], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp],f.heroID[1], 1, "Anywhere");
               }
               else if (Bring(2, AtLeast, 1, f.heroID[2], "26.Yume_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[2], 2, "Anywhere");
               }
            }
            MoveUnit(All, f.heroID[cp], cp, "Anywhere", f.location[cp]);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 4)
         {          
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            if (f.loop[cp] % 2 == 0)
            {
               f.EdgeShape(cp, 1, "40 + 1n Zealot", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
               KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            }
            else
            {
               f.EdgeShape(cp, 1, "Protoss Dark Templar", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
               KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
            }

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {                        
            f.LineShape(cp, 1, "Target", 45, 5, 75, 75);
            f.LineShape(cp, 1, "Target", 45, 5, 75, 0);
            f.LineShape(cp, 1, "Target", 225, 5, 75, 75);
            f.LineShape(cp, 1, "Protoss Dark Archon", 45, 5, 75, 75);
            f.LineShape(cp, 1, "Protoss Dark Archon", 45, 5, 75, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 225, 5, 75, 75);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {                        
            f.LineShape(cp, 1, "80 + 1n Artanis", 135, 5, 75, 75);
            f.LineShape(cp, 1, "80 + 1n Artanis", 135, 5, 75, 0);
            f.LineShape(cp, 1, "80 + 1n Artanis", 315, 5, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 5, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 5, 75, 0);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 315, 5, 75, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Artanis", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {                        
            RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);

            f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 75, 75);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 75, 0);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 315, 5, 75, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            
            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {                        
            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 75);
            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 0);
            f.LineShape(cp, 1, "40 + 1n Wraith", 225, 5, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 75, 0);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 225, 5, 75, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {                        
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 75, 75);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 75, 0);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 225, 5, 75, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            
            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }

         else if (f.loop[cp] == 9)
         {         
            SetDeaths(cp, SetTo, 1080, " `UniqueCoolTime");

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 4)
      {
         if (Bring(cp, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
         {
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 200;
            KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", cp);
         }
         else if (Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
         {
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 300;
            KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", cp);
         }
         
         else if (Bring(cp, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
         {
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 100;
            KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", cp);
         }
         else
         {
            f.SkillEnd(cp);
         }
      }
   }
}